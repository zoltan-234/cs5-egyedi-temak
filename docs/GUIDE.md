# CS5 Themes – installation guide

Custom themes for CooSpace 5  
Version 0.7.0 · Magyar verzió: UTMUTATO.md

## Contents

1. [What is this?](#1-what-is-this)
2. [Which browser do you use?](#2-which-browser-do-you-use)
3. [Downloading the file](#3-downloading-the-file)
4. [Installing in Firefox](#4-installing-in-firefox)
5. [Installing in Chrome](#5-installing-in-chrome)
6. [Installing in Edge](#6-installing-in-edge)
7. [Installing in Brave](#7-installing-in-brave)
8. [Using it](#8-using-it)
9. [Things to watch out for](#9-things-to-watch-out-for)
10. [Updating](#10-updating)
11. [Troubleshooting](#11-troubleshooting)
12. [Removing it](#12-removing-it)
13. [Licence, reporting issues](#13-licence-reporting-issues)


## 1. What is this?

**CS5 Themes** is a small browser extension for the **CooSpace 5 (CS5)** site. It lets you choose how the site looks: 19 colour themes (light, colourful, pink, dark) and 6 styles (Classic, Modern, Glass, Islands, Brutalist, Top menu), freely combined.

- Your choice **is kept** after a refresh (F5) and after restarting the browser.
- Switch with one click: click the extension icon and the picker opens.
- Free, and can be turned off or removed at any time.

> ✅ **Nothing to worry about: it only changes the looks**  
> The extension changes **only how the page looks** (colours, shapes, animations). It is safe because:

- **It runs only on the CooSpace 5 site** and has no access to any other website.
- **It sends nothing anywhere**: no server, no tracking, no analytics. Your chosen theme is stored only in your own browser.
- **It does not change any CooSpace data**: it submits nothing and does not touch your grades, messages or assignments. Turn it off and everything is exactly as before.
- **It never asks for a password** and has no access to your saved passwords, history or other tabs.
- **The source code is open**: the full code is on GitHub for anyone to inspect.
- It is an **unofficial** project, not affiliated with the operators or developers of the CooSpace site.

To be technically precise: the extension has to run on the CooSpace page in order to recolour it, which the browser gates behind a separate permission (see the install chapters). It does not read out or forward the page's content; it only adjusts the appearance (colours, sizes).


## 2. Which browser do you use?

Installation differs slightly per browser. Find yours in the table, then jump to its chapter.

| Browser | How to install | Stays after restart? | Automatic updates |
|---|---|---|---|
| **Firefox** | Signed .xpi file, one click | Yes | Yes (daily) |
| **Chrome** | Load an unpacked folder | Yes, as long as the folder stays put | No, manual |
| **Edge** | Load an unpacked folder | Yes, as long as the folder stays put | No, manual |
| **Brave** | Load an unpacked folder | Yes, as long as the folder stays put | No, manual |

> ℹ️ **Phones and tablets**  
> Chrome, Edge and Brave on Android do not support extensions, so it cannot be used there. We have not tested Firefox for Android, so it is not recommended. The extension is made for desktop computers (Windows, macOS, Linux).


## 3. Downloading the file

Every release is on the GitHub **Releases** page: `https://github.com/zoltan-234/cs5-egyedi-temak/releases/latest`

1. Open the page above. In the **Assets** list you will see two files.

   ![The GitHub Releases page: the two downloadable files](screenshots/GH-01.png)
   *The GitHub Releases page: the two downloadable files*
   
2. **For Firefox** download the file ending in `.xpi` (e.g. `cs5-temak-0.7.0.xpi`).
3. **For Chrome, Edge and Brave** download the `…-chromium.zip` file.

   ![The downloaded files: the .xpi and the -chromium.zip](screenshots/GH-02.png)
   *The downloaded files: the .xpi and the -chromium.zip*
   


## 4. Installing in Firefox

> ✅ **This is the easiest one**  
> The Firefox version is **signed** by Mozilla, so it installs simply, stays permanently and updates itself.

1. Download the `.xpi` file from the Releases page (chapter 3): click the link, or open the downloaded file.
2. Firefox asks whether to allow **github.com** to install an add-on. Click **Continue to Installation**.

   ![Firefox: permission for github.com to install an add-on](screenshots/FF-00.png)
   *Firefox: permission for github.com to install an add-on*
   
3. The **Add CS5 Themes** window appears. It shows what the extension asks for: access to data on the CooSpace 5 site only, and that it collects no data. Click **Add**.

   ![Firefox: adding CS5 Themes, with the permissions it asks for](screenshots/FF-01.png)
   *Firefox: adding CS5 Themes, with the permissions it asks for*
   
4. Check: on `about:addons` the **CS5 Themes** is listed among your extensions, switched on.

   ![Firefox: the add-on in the add-ons list](screenshots/FF-02.png)
   *Firefox: the add-on in the add-ons list*
   
5. Grant access to the CooSpace site (Firefox requires this separately, once): right-click the extension icon and choose **Always allow on unics.szte.hu**. You can also pin the icon to the toolbar there (**Pin to Toolbar**). The extension popup also has an **Allow** button that does the same.

   ![Firefox: the icon's menu: site access, pinning, removal](screenshots/FF-03.png)
   *Firefox: the icon's menu: site access, pinning, removal*
   
6. Open the CooSpace site, click the icon and choose a colour and a style. The change is instant.

> ℹ️ **Updates**  
> Firefox checks once a day for a newer version and updates itself. To check right away: `about:addons` → gear icon → **Check for Updates**.


## 5. Installing in Chrome

> ⚠️ **Important: the folder is the extension's home**  
> Chrome reads the files from the downloaded folder instead of copying them. So **do not delete or move** the folder, otherwise the extension stops.

1. Download the `…-chromium.zip` file (chapter 3) and **extract it to a permanent place**, e.g. `Documents\cs5-temak`. Right-click → **Extract All**. `manifest.json` must be directly inside the extracted folder.
2. Open the extensions page: Chrome menu (⋮) → **Extensions** → **Manage extensions**. (Or type `chrome://extensions`.)

   ![Chrome: menu → Extensions → Manage extensions](screenshots/CH-00.png)
   *Chrome: menu → Extensions → Manage extensions*
   
3. Switch on **Developer mode** in the top right, then click **Load unpacked**.

   ![Chrome: the extensions page with Developer mode on and the load button](screenshots/CH-01.png)
   *Chrome: the extensions page with Developer mode on and the load button*
   
4. Choose the extracted folder and click **Select Folder**.

   ![The folder picker: choose the extracted folder](screenshots/CH-02.png)
   *The folder picker: choose the extracted folder*
   
5. **CS5 Themes** appears in the list, with no error.

   ![Chrome: the loaded extension card](screenshots/CH-03.png)
   *Chrome: the loaded extension card*
   
6. Pin the icon: puzzle icon → the pin next to CS5 Themes.

   ![Chrome: pinning the extension to the toolbar](screenshots/CH-04.png)
   *Chrome: pinning the extension to the toolbar*
   
7. Open the CooSpace site, click the icon and choose a theme (chapter 8).

> ℹ️ **No “Allow” button needed**  
> In Chrome, Edge and Brave, access to the site is already granted on install, unlike Firefox.


## 6. Installing in Edge

> ⚠️ **Important: the folder is the extension's home**  
> Edge also reads the files from the extracted folder. **Do not delete or move** the folder.

1. Download the `…-chromium.zip` file (chapter 3) and extract it to a permanent place.
2. Open the extensions page: Edge menu (⋯) → **Extensions** → **Manage extensions**. (Or: `edge://extensions`.)

   ![Edge: menu → Extensions → Manage extensions](screenshots/ED-00.png)
   *Edge: menu → Extensions → Manage extensions*
   
3. Switch on **Developer mode** in the bottom left, then click **Load unpacked**.

   ![Edge: the extensions page with Developer mode on and the load button](screenshots/ED-01.png)
   *Edge: the extensions page with Developer mode on and the load button*
   
4. Choose the folder that contains `manifest.json` (the same folder picker as in Chrome).

   ![The folder picker: choose the extracted folder](screenshots/CH-02.png)
   *The folder picker: choose the extracted folder*
   
5. **CS5 Themes** appears in the list, with no error.

   ![Edge: the loaded extension card](screenshots/ED-02.png)
   *Edge: the loaded extension card*
   
6. Pin the icon to the toolbar: Extensions (puzzle) menu → the pin next to CS5 Themes.

   ![Edge: pinning to the toolbar and removing from the extensions menu](screenshots/ED-03.png)
   *Edge: pinning to the toolbar and removing from the extensions menu*
   
7. Open the CooSpace site and choose a theme (chapter 8).


## 7. Installing in Brave

> ⚠️ **Important: the folder is the extension's home**  
> Brave also reads the files from the extracted folder. **Do not delete or move** the folder.

1. Download the `…-chromium.zip` file (chapter 3) and extract it to a permanent place.
2. Open the extensions page: Brave menu (☰) → **Extensions** → **Manage extensions**. (Or: `brave://extensions`.)

   ![Brave: menu → Extensions → Manage extensions](screenshots/BR-00.png)
   *Brave: menu → Extensions → Manage extensions*
   
3. Switch on **Developer mode** in the top right, then click **Load unpacked**.

   ![Brave: the extensions page with Developer mode on and the load button](screenshots/BR-01.png)
   *Brave: the extensions page with Developer mode on and the load button*
   
4. Choose the folder that contains `manifest.json` (the same folder picker as in Chrome).

   ![The folder picker: choose the extracted folder](screenshots/CH-02.png)
   *The folder picker: choose the extracted folder*
   
5. **CS5 Themes** appears in the list, with no error.

   ![Brave: the loaded extension card](screenshots/BR-02.png)
   *Brave: the loaded extension card*
   
6. Pin the icon to the toolbar: puzzle icon → the pin next to CS5 Themes.

   ![Brave: pinning to the toolbar and removal](screenshots/BR-03.png)
   *Brave: pinning to the toolbar and removal*
   
7. Open the CooSpace site and choose a theme (chapter 8).

> ℹ️ **Vivaldi, Opera and other Chromium browsers**  
> Loading unpacked works the same way there (address `vivaldi://extensions` or `opera://extensions`). We have not tested these.


## 8. Using it

1. Open the CooSpace site and click the extension icon.
2. **Colours:** pick a theme (Light, Colourful, Pink, Dark). The small preview shows the colours.
3. **Style:** scroll down and pick a shape: Classic (the original), Modern, Glass, Islands, Brutalist or Top menu.
4. The two combine freely, the change is instant, and it survives closing the browser.
5. **Features:** at the bottom of the popup there are three switches (open the Scenes page on start; default mode of the groups; remember groups). Each has an **ⓘ** mark that explains what it does. All are off by default.

> ℹ️ **Back to the original**  
> Choose **Light → Eredeti** as the colour and **Klasszikus** as the style: the page looks exactly as it does without the extension.


## 9. Things to watch out for

- **Chrome, Edge, Brave:** **do not delete, rename or move** the extracted folder. If you do, the extension switches off with an error; put it back or load it again.
- **Do not extract into the Downloads folder**, where it is easily deleted. Pick a permanent place.
- **Chrome/Edge warning:** at startup a message about “developer mode extensions” may appear. This is normal; close it, the extension works.
- **Firefox:** the Allow button is pressed once. After that it works on every CooSpace page.
- **Manual updates** (Chrome, Edge, Brave): see the next chapter.
- The effect is visible only on the CooSpace 5 site. It changes no other website.


## 10. Updating

**Firefox:** automatic, nothing to do.

**Chrome, Edge, Brave:**

1. Download the new `…-chromium.zip` from the Releases page.
2. Extract it **into the same folder**, over the old files (overwrite).
3. Open the extensions page and click **Reload** (⟳) on the CS5 Themes card.
4. Press F5 on the CooSpace site.


## 11. Troubleshooting

| What is wrong? | Fix |
|---|---|
| The page does not change | In Firefox press **Allow** in the popup, or choose **Always allow on unics.szte.hu** in the icon's right-click menu. Press F5. Check that you are on the CooSpace 5 site. |
| The Allow button does not go away (Firefox) | Click it again and answer the browser prompt with **Allow**. If it still fails, restart Firefox. |
| The extension vanished after a restart (Chrome/Edge/Brave) | The extracted folder was probably deleted or moved. Extract it again to a permanent place and load it. |
| Error on the extension card | Open the Errors button and send the text via GitHub Issues. Also try the Reload button. |
| Something looks wrong (unreadable text, white box) | Take a screenshot and tell us which theme and style. Switch to another theme meanwhile. |
| The page feels slow | The Glass style (blur) can be heavier on weaker machines. Switch to Modern or Classic. |


## 12. Removing it

After removal the page returns to its original look and all extension data is deleted from your browser.

1. **Firefox:** right-click the extension icon → **Remove Extension** (or `about:addons` → **…** → **Remove**).

   ![Firefox: the icon's menu: site access, pinning, removal](screenshots/FF-03.png)
   *Firefox: the icon's menu: site access, pinning, removal*
   
2. **Chrome:** puzzle icon → the **⋮** next to CS5 Themes → **Remove from Chrome** (or `chrome://extensions` → **Remove**).

   ![Chrome: removing the extension](screenshots/CH-05.png)
   *Chrome: removing the extension*
   
3. **Edge:** Extensions (puzzle) menu → **⋯** → **Remove from Microsoft Edge**.

   ![Edge: pinning to the toolbar and removing from the extensions menu](screenshots/ED-03.png)
   *Edge: pinning to the toolbar and removing from the extensions menu*
   
4. **Brave:** puzzle icon → the **⋮** next to CS5 Themes → **Remove from Brave**.

   ![Brave: pinning to the toolbar and removal](screenshots/BR-03.png)
   *Brave: pinning to the toolbar and removal*
   
5. For Chrome/Edge/Brave you can then delete the extracted folder too.


## 13. Licence, reporting issues

- **Licence:** PolyForm Noncommercial 1.0.0. Free to use, copy and modify for **non-commercial purposes**; it may not be used to make money. The fonts (Inter, Manrope) are under the SIL OFL licence.
- **Unofficial** project, not affiliated with the operators or developers of the CooSpace site.
- **Found a bug or have an idea?** Write on the GitHub **Issues** page: `https://github.com/zoltan-234/cs5-egyedi-temak/issues`. You can attach a screenshot.
- The code is public: `https://github.com/zoltan-234/cs5-egyedi-temak`

