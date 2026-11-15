import { test, expect } from '@playwright/test';
import { reconciliationData }from '../test-data/reconciliationData';
import { ReconciliationPage }from '../pages/Reconciliationpage';
import { loginData}from '../test-data/loginData';
import { LoginPage }from '../pages/LoginPage';
import { existsSync } from 'fs';


test(
    'Valid Login',
    async ({ page }) => {

        const loginPage =
            new LoginPage(page);

        await loginPage.navigate();

        await loginPage.login(
            loginData.validUsername,
            loginData.validPassword
        );

        await expect(
            page.locator('h1')
        ).toContainText(
            'ETL Reconciliation Portal'
        );

           // Pause for observation

        await page.waitForTimeout(
            2500
        );
    }
);

test(
    'Invalid Login',
    async ({ page }) => {

        const loginPage =
            new LoginPage(page);

        await loginPage.navigate();

       await loginPage.login(
            loginData.invalidUsername,
            loginData.invalidPassword
        );

await page.screenshot({
    path: 'invalid-login-debug.png',
    fullPage: true
});

await page.waitForTimeout(3000);


        await expect(
            page.getByText(
                'Invalid Username or Password'
            )
        ).toBeVisible();

           // Pause for observation

        await page.waitForTimeout(
            2500
        );
    }
);


test(
    'ETL Reconciliation Test',
    async ({ page }) => {

          const loginPage =
            new LoginPage(page);

        await loginPage.navigate();

        await loginPage.login(
            loginData.validUsername,
            loginData.validPassword
        );
      
        const reconPage =
            new ReconciliationPage(page);

        // await reconPage.navigate();

        await reconPage.uploadSourceFile(
            'D:/ETL-Recon-framework/Data/source_target/source_10-11-2026-10-46.xlsx'
        );

        await reconPage.uploadTargetFile(
            'D:/ETL-Recon-framework/Data/source_target/target_10-11-2026-10-46.xlsx'
        );

        await reconPage.clickCompare();

        await expect(
            page.locator('#matched')
        ).toHaveText(
            reconciliationData.matched
        );

        await expect(
            page.locator('#mismatched')
        ).toHaveText(
            reconciliationData.mismatched
        );

        await expect(
            page.locator('#missing')
        ).toHaveText(
            reconciliationData.missing
        );

        await expect(
            page.locator('#additional')
        ).toHaveText(
            reconciliationData.additional
        );

        await expect(
            page.locator('#duplicates')
        ).toHaveText(
            reconciliationData.duplicates
        );

        console.log(
            'Reconciliation Validation Passed'
        );
           // Pause for observation

        await page.waitForTimeout(
            2500
        );
    }
);

test(
    'Verify Report Download',
    async ({ page }) => {

          const loginPage =
            new LoginPage(page);

        await loginPage.navigate();

        await loginPage.login(
            loginData.validUsername,
            loginData.validPassword
        );


        const reconPage =
            new ReconciliationPage(page);

        // await reconPage.navigate();

        await reconPage.uploadSourceFile(
            'D:/ETL-Recon-framework/Data/source_target/source_10-11-2026-10-46.xlsx'
        );

        await reconPage.uploadTargetFile(
            'D:/ETL-Recon-framework/Data/source_target/target_10-11-2026-10-46.xlsx'
        );

        await reconPage.clickCompare();

        const downloadPromise =
            page.waitForEvent('download');

        await reconPage.downloadReport();

        const download =
            await downloadPromise;

        const fileName =
            download.suggestedFilename();

        const filePath =
            `downloads/${fileName}`;

        // Save file physically

        await download.saveAs(
            filePath
        );

        console.log(
            `Downloaded File: ${fileName}`
        );

        console.log(
            `Saved To: ${filePath}`
        );

        // Validate filename

        expect(fileName)
            .toContain(
                'reconciliation_report'
            );

        console.log(
            'Filename Validation Passed'
        );

        // Validate extension

        expect(fileName)
            .toMatch(/\.xlsx$/);

        console.log(
            'Excel Extension Validation Passed'
        );

        // Validate file exists

        expect(
            existsSync(filePath)
        ).toBeTruthy();

        console.log(
            'File Exists Validation Passed'
        );

        console.log(
            'Download Validation Passed'
        );

           // Pause for observation

        await page.waitForTimeout(
            2500
        );
    }
);


test(
    'Verify Missing Target File Validation',
    async ({ page }) => {

          const loginPage =
            new LoginPage(page);

        await loginPage.navigate();

        await loginPage.login(
            loginData.validUsername,
            loginData.validPassword
        );


        const reconPage =
            new ReconciliationPage(page);

        // await reconPage.navigate();

        await reconPage.uploadSourceFile(
            'D:/ETL-Recon-framework/Data/source_target/source_10-11-2026-10-46.xlsx'
        );

        await reconPage.clickCompare();

        // Verify still on upload page

        await expect(
            page.locator('h1')
        ).toContainText(
            'ETL Reconciliation Portal'
        );

        console.log(
            'Form Submission Blocked'
        );

        // Pause for observation

        await page.waitForTimeout(
            2500
        );
    }
);

test(
    'Verify Empty Source File Validation',
    async ({ page }) => {

  const loginPage =
            new LoginPage(page);

        await loginPage.navigate();

        await loginPage.login(
            loginData.validUsername,
            loginData.validPassword
        );

        
        const reconPage =
            new ReconciliationPage(page);

        // await reconPage.navigate();

        await reconPage.uploadSourceFile(
            'D:/ETL-Recon-framework/Data/source_target/empty.xlsx'
        );

        await reconPage.uploadTargetFile(
            'D:/ETL-Recon-framework/Data/source_target/target_10-11-2026-10-46.xlsx'
        );

        await reconPage.clickCompare();

        await expect(
            page.getByText(
                'Source file contains no records.'
            )
        ).toBeVisible();

        console.log(
            'Empty Source File Validation Passed'
        );

        // Pause for observation

        await page.waitForTimeout(
            2500
        );
    }
);