const { chromium } = require('playwright');

async function runTasks() {
  const browser = await chromium.launch();
  const context = await browser.newContext();

  try {
    // Task 1: Take screenshot of github.com
    console.log('Task 1: Taking screenshot of https://github.com...');
    const page1 = await context.newPage();
    await page1.goto('https://github.com', { waitUntil: 'networkidle' });
    await page1.screenshot({ path: 'github-screenshot.png', fullPage: true });
    console.log('✓ Screenshot saved to github-screenshot.png');
    await page1.close();

    // Task 2: Extract page title from news.ycombinator.com
    console.log('\nTask 2: Extracting title from https://news.ycombinator.com...');
    const page2 = await context.newPage();
    await page2.goto('https://news.ycombinator.com', { waitUntil: 'networkidle' });
    const title = await page2.title();
    console.log(`✓ Page title: "${title}"`);
    await page2.close();

    // Task 3: Check if example.com contains "documentation"
    console.log('\nTask 3: Checking if example.com contains "documentation"...');
    const page3 = await context.newPage();
    await page3.goto('https://example.com', { waitUntil: 'networkidle' });
    const content = await page3.content();
    const containsDocumentation = content.toLowerCase().includes('documentation');
    console.log(`✓ Contains "documentation": ${containsDocumentation}`);
    await page3.close();

  } catch (error) {
    console.error('Error:', error.message);
  } finally {
    await browser.close();
  }
}

runTasks();
