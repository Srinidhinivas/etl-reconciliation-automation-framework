import { Page } from '@playwright/test';

export class ReconciliationPage {

    constructor(private page: Page) {}

    sourceFile = 'input[name="source_file"]';

    targetFile = 'input[name="target_file"]';

    compareButton = 'button[type="submit"]';

    downloadButton = '.download-btn';

    async navigate() {

        await this.page.goto(
            'http://127.0.0.1:5000'
        );
    }

    async uploadSourceFile(
        filePath: string
    ) {

        await this.page.setInputFiles(
            this.sourceFile,
            filePath
        );
    }

    async uploadTargetFile(
        filePath: string
    ) {

        await this.page.setInputFiles(
            this.targetFile,
            filePath
        );
    }

    async clickCompare() {

        await this.page.click(
            this.compareButton
        );
    }

    async downloadReport() {

    await this.page.click(
        this.downloadButton
    );
}

   async getCurrentUrl() {

    return this.page.url();
}
}