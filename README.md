<a href="https://github.com/lintonjr/algoritmos_orlewilson">
    <img src="https://d3pwz8qrais8b7.cloudfront.net/portal-wyden/public/custom-uploads/wyden-footer.png" alt="Aimeos logo" title="Trabalho de Algoritmos" align="right" height="60" />
</a>

# Trabalho de Algoritmos - Prof. Orlewilson

Trabalho de [Algoritmos](https://github.com/lintonjr/algoritmos_orlewilson) da disciplina lecionada pelo Professor Orlewilson na FMF.

[![Algoritmos Demo](http://oi66.tinypic.com/10da1lg.jpg)](http://oi66.tinypic.com/10da1lg.jpg)

## Conteúdo

- [22/05/2019](#Parte1)
  - [Questão 1](#Questão-1)
  - [Questão 2](#Questão-2)
  - [Database](#database)
- [Page setup](#page-setup)
  - [Upload the page tree file](#upload-the-page-tree-file)
  - [Go to the import view](#go-to-the-import-view)
  - [Import the uploaded page tree file](#import-the-uploaded-page-tree-file)
- [License](#license)
- [Links](#links) -->

## Parte1

Questões a serem entregues e defendidas **Data: 22/05/2019 - Adiada**.

### Questão 1

- Elabore um fluxograma e desenvolva em linguagem C ou Python em cada item a seguir: (Questões de A à L)
- Sabendo que A=5, B=4 e C=3 e D=6, informe se as expressões abaixo são verdadeiras ou
  falsas.
  I. (A > C) e (C <= D).

  II. (A+B) > 10 ou (A+B) = (C+D).

  III. (A>=C) e (D >= C).

  (A) F, F e F.

  (B) V, F e V.

  (C) V, V e V.

  (D) F, F e V.

  (E) V, V e F.

### Questão 2

- Considere as seguintes atribuições: R = 2, S = 5, T = -1, X = 3, Y = 1 e Z = 0. Resolva as
  expressões abaixo:
  • A <- (Z >= 5) or (T > Z) and (X – Y + R > 3 \_ Z)

  • B <- (T + 3 >= 4) and not (3 _ R/2 < S _ 3)

  • C <- (X == 2) or (Y == 1) AND ((Z == 0) OR (R > 3)) AND (S < 10)

  • D <- (R <> S) OR NOT (R < X) AND (4327 _ X _ S \_ Z == 0)

<!-- ### TYPO3 extension repository

If you want to install Aimeos into your existing TYPO3 installation, the [Aimeos extension from the TER](https://typo3.org/extensions/repository/view/aimeos) is recommended. You can download and install it directly from the Extension Manager of your TYPO3 instance.

For new TYPO3 installations, there's a 1-click [Aimeos distribution](https://typo3.org/extensions/repository/view/aimeos_dist) available too. Choose the Aimeos distribution from the list of available distributions in the Extension Manager and you will get a completely set up shop system including demo data for a quick start.

### Composer

The latest version can be installed via composer too. This is especially useful if you want to create new TYPO3 installations automatically or play with the latest code. You need to install the [composer](https://getcomposer.org/) package first if it isn't already available:

```
php -r "readfile('https://getcomposer.org/installer');" | php -- --filename=composer
```

In order to tell composer what it should install, you have to create a basic `composer.json` file in the directory of you VHost. It should look similar to this one:

```json
{
  "name": "vendor/mysite",
  "description": "My new TYPO3 web site",
  "require": {
    "typo3/cms": "~8.7",
    "aimeos/aimeos-typo3": "~19.4"
  },
  "extra": {
    "typo3/cms": {
      "cms-package-dir": "{$vendor-dir}/typo3/cms",
      "web-dir": "public"
    }
  },
  "scripts": {
    "post-install-cmd": ["Aimeos\\Aimeos\\Custom\\Composer::install"],
    "post-update-cmd": ["Aimeos\\Aimeos\\Custom\\Composer::install"]
  }
}
```

It will install TYPO3 and the latest Aimeos TYPO3 extension in the `./public/` directory. Afterwards, the Aimeos composer script will be executed which copies some required files and adds a link to the Aimeos extensions placed in the `./ext/` directory. To start installation, execute composer on the command line in the directory where your `composer.json` is stored:

```
composer update
```

## TYPO3 setup

### Database setup

Starting with Aimeos 18.10 and TYPO3 9.5, it's possible to define the charset and collation for newly created MySQL tables. In case you want to use a NoSQL data store like ElasticSearch for Aimeos products, you need to use a binary collation `utf8mb4_bin` in your `typo3conf/LocalConfiguration.php` file **before** the tables are created:

```
'DB' => [
    'Connections' => [
        'Default' => [
            'tableoptions' => [
                'charset' => 'utf8mb4',
                'collate' => 'utf8mb4_bin',
            ],
            // ...
        ],
    ],
],
```

**Caution:** If you use MySQL < 5.7, you have to use `utf8` and `utf8_bin` instead because those MySQL versions can't handle the long indexes created by `utf8mb4` (up to four bytes per character) and you will get errors like `1071 Specified key was too long; max key length is 767 bytes`:

```
'DB' => [
    'Connections' => [
        'Default' => [
            'tableoptions' => [
                'charset' => 'utf8',
                'collate' => 'utf8_bin',
            ],
            // ...
        ],
    ],
],
```

### Extension

- Log into the TYPO3 back end
- Click on ''Admin Tools::Extension Manager'' in the left navigation
- Click the icon with the little plus sign left from the Aimeos list entry (looks like a lego brick)

**Caution:** Install the **RealURL extension before the Aimeos extension** to get nice looking URLs. Otherwise, RealURL doesn't rewrite the parameters even if you install RealURL afterwards!

![Install Aimeos TYPO3 extension](https://aimeos.org/docs/images/Aimeos-typo3-extmngr-install.png)

### Database

Afterwards, you have to execute the update script of the extension to create the required database structure:

![Execute update script](https://aimeos.org/docs/images/Aimeos-typo3-extmngr-update-7.x.png)

## Page setup

The page setup for an Aimeos web shop is easy if you import the [standard page tree for TYPO3 8.7/9.5](https://aimeos.org/docs/TYPO3/Install_Aimeos/Setup_pages#Download) into your TYPO3 installation.

### Go to the import view

- In Web::Page, root page (the one with the globe)
- Right click on the globe
- Move the cursor to "Branch actions"
- In the sub-menu, click on "Import from .t3d"

![Go to the import view](https://aimeos.org/docs/images/Aimeos-typo3-pages-menu.png)

### Upload the page tree file

- In the page import dialog
- Select the "Upload" tab (2nd one)
- Click on the "Select" dialog
- Choose the file you've downloaded
- Press the "Upload files" button

![Upload the page tree file](https://aimeos.org/docs/images/Aimeos-typo3-pages-upload.png)

### Import the uploaded page tree file

- In Import / Export view
- Select the uploaded file from the drop-down menu
- Click on the "Preview" button
- The pages that will be imported are shown below
- Click on the "Import" button that has appeared
- Confirm to import the pages

![Import the uploaded page tree file](https://aimeos.org/docs/images/Aimeos-typo3-pages-import.png)

Now you have a new page "Shop" in your page tree including all required sub-pages.

## License

The Aimeos TYPO3 extension is licensed under the terms of the GPL Open Source
license and is available for free.

## Links

- [Web site](https://aimeos.org/integrations/typo3-shop-extension/)
- [Documentation](https://aimeos.org/docs/TYPO3)
- [Forum](https://aimeos.org/help/typo3-extension-f16/)
- [Issue tracker](https://github.com/aimeos/aimeos-typo3/issues)
- [Source code](https://github.com/aimeos/aimeos-typo3) -->
