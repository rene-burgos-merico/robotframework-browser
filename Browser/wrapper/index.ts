import { IPlaywrightServer, PlaywrightService } from './generated/playwright_grpc_pb';
import { chromium, firefox, webkit, Browser, BrowserContext, Page } from 'playwright';
import { sendUnaryData, ServerUnaryCall, Server, ServerCredentials } from 'grpc';
import { Response, Request } from './generated/playwright_pb';

// This is necessary for improved typescript inference
/*
 * If obj is not trueish call callback with new Error containing message
 */
function exists<T1, T2>(obj: T1, callback: sendUnaryData<T2>, message: string): asserts obj is NonNullable<T1> {
    if (!obj) {
        callback(new Error(message), null);
    }
}

// Can't have an async constructor, this is a workaround
async function createBrowserState(browserType: string): Promise<BrowserState> {
    const headless = true;
    let browser;
    if (browserType === 'firefox') {
        browser = await firefox.launch({ headless: headless });
    } else if (browserType === 'chrome') {
        browser = await chromium.launch({ headless: headless });
    } else if (browserType === 'webkit') {
        browser = await webkit.launch();
    } else {
        throw new Error('unsupported browser');
    }
    const context = await browser.newContext();
    const defaultTimeout = parseInt(process.env.DEFAULT_TIMEOUT!);
    context.setDefaultTimeout(defaultTimeout);
    const page = await context.newPage();
    return new BrowserState(browser, context, page);
}

class BrowserState {
    constructor(browser: Browser, context: BrowserContext, page: Page) {
        this.browser = browser;
        this.context = context;
        this.page = page;
    }
    browser: Browser;
    context: BrowserContext;
    page: Page;
}

function emptyWithLog(text: string): Response.Empty {
    const response = new Response.Empty();
    response.setLog(text);
    return response;
}

// If function f needs context like `this` it should be an arrow function
async function tryCatch<T1>(f: Function, args: any, callback: sendUnaryData<T1>) {
    try {
        await f(args);
    } catch (e) {
        callback(e, null);
    }
}

class PlaywrightServer implements IPlaywrightServer {
    private browserState?: BrowserState;

    openUrl = async (url: string, callback: sendUnaryData<Response.Empty>) => {
        exists(this.browserState, callback, 'Tried to open URl but had no browser open');
        await this.browserState.page.goto(url);
    };

    async closeBrowser(call: ServerUnaryCall<Request.Empty>, callback: sendUnaryData<Response.Empty>): Promise<void> {
        exists(this.browserState, callback, 'Tried to close browser but none was open');
        await this.browserState.browser.close();
        this.browserState = undefined;
        console.log('Closed browser');
        const response = emptyWithLog('Closed browser');
        callback(null, response);
    }

    async openBrowser(
        call: ServerUnaryCall<Request.openBrowser>,
        callback: sendUnaryData<Response.Empty>,
    ): Promise<void> {
        const browserType = call.request.getBrowser();
        const url = call.request.getUrl();
        console.log('Open browser: ' + browserType);
        this.browserState = await createBrowserState(browserType);
        if (url) {
            await this.openUrl(url, callback);
            callback(null, emptyWithLog(`Succesfully opened browser ${browserType} to ${url}.`));
        } else {
            callback(null, emptyWithLog(`Succesfully opened browser ${browserType}.`));
        }
    }

    async goTo(call: ServerUnaryCall<Request.goTo>, callback: sendUnaryData<Response.Empty>): Promise<void> {
        const url = call.request.getUrl();
        console.log('Go to URL: ' + url);

        await tryCatch(this.openUrl, [url, callback], callback);
        const response = emptyWithLog('Succesfully opened URL');
        callback(null, response);
    }

    async getTitle(call: ServerUnaryCall<Request.Empty>, callback: sendUnaryData<Response.String>): Promise<void> {
        exists(this.browserState, callback, 'Tried to get title, no open browser');
        console.log('Getting title');
        const title = await this.browserState.page.title();
        const response = new Response.String();
        response.setBody(title);
        callback(null, response);
    }

    async getUrl(call: ServerUnaryCall<Request.Empty>, callback: sendUnaryData<Response.String>): Promise<void> {
        exists(this.browserState, callback, 'Tried to get page URL, no open browser');
        console.log('Getting URL');
        const url = this.browserState.page.url();
        const response = new Response.String();
        response.setBody(url);
        callback(null, response);
    }

    async getTextContent(
        call: ServerUnaryCall<Request.selector>,
        callback: sendUnaryData<Response.String>,
    ): Promise<void> {
        exists(this.browserState, callback, 'Tried to find text on page, no open browser');
        const selector = call.request.getSelector();
        const content = await this.browserState.page.textContent(selector);
        const response = new Response.String();
        response.setBody(content?.toString() || '');
        callback(null, response);
    }

    // TODO: work some of getDomProperty and getBoolProperty's duplicate code into a root function
    async getDomProperty(
        call: ServerUnaryCall<Request.getDomProperty>,
        callback: sendUnaryData<Response.String>,
    ): Promise<void> {
        exists(this.browserState, callback, 'Tried to get DOM property, no open browser');
        const selector = call.request.getSelector();
        const property = call.request.getProperty();

        const element = await this.browserState.page.$(selector);
        exists(element, callback, "Couldn't find element: " + selector);

        const result = await element.getProperty(property);
        const content = await result.jsonValue();
        console.log(`Retrieved dom property for element ${selector} containing ${content}`);

        const response = new Response.String();
        response.setBody(content);
        callback(null, response);
    }

    async getBoolProperty(
        call: ServerUnaryCall<Request.getDomProperty>,
        callback: sendUnaryData<Response.Bool>,
    ): Promise<void> {
        exists(this.browserState, callback, 'Tried to get DOM property, no open browser');
        const selector = call.request.getSelector();
        const property = call.request.getProperty();

        const element = await this.browserState.page.$(selector);
        exists(element, callback, "Couldn't find element: " + selector);

        const result = await element.getProperty(property);
        const content = await result.jsonValue();
        console.log(`Retrieved dom property for element ${selector} containing ${content}`);

        const response = new Response.Bool();
        response.setBody(content || false);
        callback(null, response);
    }

    async inputText(call: ServerUnaryCall<Request.inputText>, callback: sendUnaryData<Response.Empty>): Promise<void> {
        exists(this.browserState, callback, 'Tried to input text, no open browser');
        const inputText = call.request.getInput();
        const selector = call.request.getSelector();
        await this.browserState.page.fill(selector, inputText);

        const response = emptyWithLog('Input text: ' + inputText);
        callback(null, response);
    }

    async clickButton(call: ServerUnaryCall<Request.selector>, callback: sendUnaryData<Response.Empty>): Promise<void> {
        exists(this.browserState, callback, 'Tried to click button, no open browser');

        const selector = call.request.getSelector();
        await this.browserState.page.click(selector);
        const response = emptyWithLog('Clicked button: ' + selector);
        callback(null, response);
    }

    async checkCheckbox(
        call: ServerUnaryCall<Request.selector>,
        callback: sendUnaryData<Response.Empty>,
    ): Promise<void> {
        exists(this.browserState, callback, 'Tried to check checkbox, no open browser');
        const selector = call.request.getSelector();
        await this.browserState.page.check(selector);
        const response = emptyWithLog('Checked checkbox: ' + selector);
        callback(null, response);
    }
    async uncheckCheckbox(
        call: ServerUnaryCall<Request.selector>,
        callback: sendUnaryData<Response.Empty>,
    ): Promise<void> {
        exists(this.browserState, callback, 'Tried to uncheck checkbox, no open browser');
        const selector = call.request.getSelector();
        await this.browserState.page.uncheck(selector);
        const response = emptyWithLog('Unhecked checkbox: ' + selector);
        callback(null, response);
    }

    async health(call: ServerUnaryCall<Request.Empty>, callback: sendUnaryData<Response.String>): Promise<void> {
        const response = new Response.String();
        response.setBody('OK');
        callback(null, response);
    }

    async screenshot(
        call: ServerUnaryCall<Request.screenshot>,
        callback: sendUnaryData<Response.Empty>,
    ): Promise<void> {
        exists(this.browserState, callback, 'Tried to take screenshot, no open browser');
        // Add the file extension here because the image type is defined by playwrights defaults
        const path = call.request.getPath() + '.png';
        console.log(`Taking a screenshot of current page to ${path}`);
        await this.browserState.page.screenshot({ path: path });

        const response = emptyWithLog('Succesfully took screenshot');
        callback(null, response);
    }
}

const server = new Server();
server.addService<IPlaywrightServer>(PlaywrightService, new PlaywrightServer());
const port = process.env.PORT || '0';
server.bind(`localhost:${port}`, ServerCredentials.createInsecure());
console.log(`Listening on ${port}`);
server.start();
