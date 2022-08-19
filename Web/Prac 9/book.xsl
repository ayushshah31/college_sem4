<xsl:stylesheet version="1.0" xmlns:xsl = "https://www.w3.org/1999/XSL/Transform" >

<xsl:template match="/class">

    <html>
        <body>
            <h2>Book List</h2>
            <br />
            <table border="1">
                <tr bgcolor="green">
                    <th>Author</th>
                    <th>Year</th>
                    <th>Price</th>
                </tr>

                <xsl:for-each select="book">
                    <tr>
                        <td><xsl:value-of select="title" /></td>
                        <td><xsl:value-of select="author" /></td>
                        <td><xsl:value-of select="price" /></td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
    </html>

</xsl:template>
</xsl:stylesheet>