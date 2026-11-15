import { Page } from '@playwright/test';

export class LoginPage {

    constructor(
        private page: Page
    ) {}

    username =
        'input[name="username"]';

    password =
        'input[name="password"]';

    loginButton =
        'button[type="submit"]';

    async navigate() {

        await this.page.goto(
            'http://127.0.0.1:5000'
        );
    }

    async login(
        user: string,
        pass: string
    ) {

        await this.page.fill(
            this.username,
            user
        );

        await this.page.fill(
            this.password,
            pass
        );

        await this.page.click(
            this.loginButton
        );
    }
}