import { chromium } from 'playwright';
import path from 'node:path';
const B = process.argv[2];
const url = f => 'file://' + path.join(B, f);

const HDR = `<div style="width:100%;font-family:Arial,Helvetica,sans-serif;font-size:7pt;
  color:#98a1a9;padding:0 22mm;margin:0;-webkit-print-color-adjust:exact">
  <div style="display:flex;justify-content:space-between;border-bottom:.5px solid #dfe3e6;padding-bottom:3px">
    <span style="letter-spacing:.06em">COLLABORATIVE TRAINING CONE SYSTEM</span>
    <span>Design Specification &middot; Revision 1.0</span>
  </div></div>`;
const FTR = `<div style="width:100%;font-family:Arial,Helvetica,sans-serif;font-size:7.5pt;
  color:#98a1a9;padding:0 22mm;margin:0;-webkit-print-color-adjust:exact">
  <div style="display:flex;justify-content:space-between;border-top:.5px solid #dfe3e6;padding-top:4px">
    <span>Senior Learning Project 2026&ndash;2027</span>
    <span style="color:#0f5666;font-weight:700"><span class="pageNumber"></span>&nbsp;/&nbsp;<span class="totalPages"></span></span>
  </div></div>`;

const browser = await chromium.launch();
const page = await browser.newPage();

async function render(src, out, opts = {}) {
  await page.goto(url(src), { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: path.join(B, out), format: 'A4', printBackground: true, ...opts });
}

await render('cover.html', 'cover.pdf', { margin: { top: '0', bottom: '0', left: '0', right: '0' } });
await render('body.html', 'body.pdf', {
  displayHeaderFooter: true, headerTemplate: HDR, footerTemplate: FTR,
  margin: { top: '20mm', bottom: '18mm', left: '22mm', right: '22mm' },
});
if (process.argv[3] === 'toc') {
  await render('toc.html', 'toc.pdf', { margin: { top: '20mm', bottom: '18mm', left: '22mm', right: '22mm' } });
}
await browser.close();
console.log('rendered');
