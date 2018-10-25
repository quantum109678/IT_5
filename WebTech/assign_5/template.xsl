<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<html>
			<body>
				<table>
					<tr>
						<th>Name</th>
						<th>Genre</th>
						<th>Venue</th>
					</tr>
					<xsl:for-each select="concert/bookticket">
						<xsl:if test="genre = 'Pop'">
							<tr bgcolor="green">
								<td><xsl:value-of select="bind/name"/></td>
								<td><xsl:value-of select="genre"/></td>
								<td><xsl:value-of select="bind/place"/></td>
							</tr>
						</xsl:if>
						<xsl:if test="genre = 'Classical'">
							<tr bgcolor="yellow">
								<td><xsl:value-of select="bind/name"/></td>
								<td><xsl:value-of select="genre"/></td>
								<td><xsl:value-of select="bind/place"/></td>
							</tr>
						</xsl:if>
						<xsl:if test="genre = 'Instrumental'">
							<tr bgcolor="#33d4ff">
								<td><xsl:value-of select="bind/name"/></td>
								<td><xsl:value-of select="genre"/></td>
								<td><xsl:value-of select="bind/place"/></td>
							</tr>
						</xsl:if>
					</xsl:for-each>
				</table>
			</body>
		</html>
	</xsl:template>

</xsl:stylesheet>
