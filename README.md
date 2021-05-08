# BAIS:6040:0EXP Class Materials

# Introduction
This repository is a collection of resources for the class BAIS:6040:0EXP for Spring 2021, taught at the Univeristy of Iowa, College of Business.

All these are also in ICON, but this repository has a number of benefits:
1. Easier to stay up to date - this is updated far more frequently than ICON is, you get access to more information sooner.
2. A package of all contents - no downloading 1 at a time and self organization.
3. Honestly, far easier for me. I work in Git all the time anyways

# Format/Structure of Project
## Overall Format
The format, regardless of the folder, will have a phase associated with it. As a reminder:

| Phase | Modules | Topic |
|-------| --------| ------|
| Phase 1 | Modules 0-3.5ish | Basic Python |
| Phase 2 | Modules 3.5 - 7 | Analysis/sources |
| Phase 3 | Modules 7+ | Machine Learning |

## Folders and Contents

| Folder | Purpose |
|--------|---------|
|data    | Data Sources we'll reference for projects/homework/etc |
| Handouts | Various PDFs/word documents that's more informational in nature |
|Homework | Homework Answers |
|Notebooks | The Jupyter Notebooks |
|Slides  | The slides |

## Naming Conventions
Most of the names are intended to be consistent between the Notebook and Slides folders.  The format is:

```
[module].[lecture].[subpart]
```
For example, if we're in week 3, and lecture 4, then the corresponding notebook would be:
```
03.04.*
```

The goal is to make this easier to follow, so the notebooks can be split up for a specific lecture.  In the above case, if we have 2 notebooks then the files would be:
```text
03.04.01.ipynb
03.04.02.ipynb
```

Which relates to the slide:
```text
03.04.pptx
```

# Working with the Repository

Please see the supplemental lecture for Modules 0 and 1 for more detailed information.  In summary:

## Keeping up to date with the code (without PyCharm/etc)
1. Click the Code button with the down-arrow (green button)
2. Click on "Open with Github Desktop"
    * If not installed, it will install for you.  Launch it and fill out the details.
    * You do NOT need a Github account to use it.  If you do, sign in, if you don't then don't.
    
3. Once Github Desktop is running, go back to this page, click the Code button again and copy the text in the HTTPS box.
4. Go back to Github Desktop and select "Clone a Repository" and paste the link from #3, pick your path, and click "Clone"

To update code from the repository on a regular basis:
1. Within Github Desktop click "Fetch Origin"
2. If changes were detected, click the "Pull Origin"

Please see supplemental lecture 0 for more information on this.

## Keeping up to date with the code (With PyCharm)
1. Install Git for Windows (search and download)
2. Open PyCharm
3. Click on Git -> Clone
4. Paste in the URL from Github (green box download at the top of this page, select the HTTPS link presented)
5. Set directory, and click "Clone"

More documentation is found at:
[https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html)

You can also log into Github directly within pycharm and work with it that way.

Module 1's supplemental talks about using git within PyCharm.

## Keeping up to date with the code (Without Either)
If you're not using either of the two options, you can download a zip file of the contents on a regular basis.  I'd aim for ~1 time a week where you download the zip file, and unzip it to a convenient place (likely removing the old version), and navigating normally to it.
