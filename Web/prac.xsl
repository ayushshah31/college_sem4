<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" indent="yes" encoding="UTF-8" />
<xsl:template match="/">
    <html>
        <head>
            <title>Library</title>
        </head>
        <body>
            <table>
            <tr>
                <th>Name</th>
                <th>Author</th>
                <th>Publisher</th>
                <th>Year</th>
            </tr>
                <xsl:for-each select="Library/book">
                    <tr>
                        <td><xsl:value-of select="name" /></td>
                        <td><xsl:value-of select="author" /></td>
                        <td><xsl:value-of select="publisher" /></td>
                        <td><xsl:value-of select="year" /></td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>