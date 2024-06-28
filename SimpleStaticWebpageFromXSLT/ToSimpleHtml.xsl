<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- Define the template for the root element -->
    <xsl:template match="/rows">
        <html>
            <head>
                <title>Locations</title>
                <link rel="stylesheet" type="text/css" href="styles.css"/>
            </head>
            <body>
                <div class="container">
                    <xsl:apply-templates select="row"/>
                </div>
            </body>
        </html>
    </xsl:template>

    <!-- Define the template for each row -->
    <xsl:template match="row">
        <div class="location-block">
            <h2><xsl:value-of select="location"/></h2>
            <p><strong>Area:</strong> <xsl:value-of select="area"/></p>
            <p><a href="{concat('https://en.wikipedia.org', wiki_link)}" target="_blank">Wikipedia</a></p>
            <p><a href="{heritage_link}" target="_blank">Heritage Gateway</a></p>
            <p><strong>Coordinates:</strong> <xsl:value-of select="coordinates"/></p>
            <iframe
                    width="600"
                    height="450"
                    style="border:0"
                    loading="lazy"
                    allowfullscreen="true"
                    src="http://maps.google.com/maps?q={latitude},{longitude}&amp;z=16&amp;output=embed">
            </iframe>
        </div>
    </xsl:template>

</xsl:stylesheet>