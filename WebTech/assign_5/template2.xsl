<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<html>
			<body>
				<table cellpadding="5" cellspacing="5">
					<tr>
						<th>Name</th>
						<th>Venue</th>
						<th>Date</th>
						<th>Genre</th>
						<th>Performer</th>
						<th>Ticket</th>
						<th>Seller</th>
						<th>Discount</th>
					</tr>
					<xsl:for-each select="concert/bookticket">
						<xsl:if test="bind/place/addr = 'Mangalore' and ticktype/ticket/price &lt; 100 and datetime/show/month = 'April'">
							<xsl:if test="discount &gt; 0">
								<tr bgcolor="#33d4ff">
									<td><xsl:value-of select="bind/name"/></td>
									<td><xsl:value-of select="bind/place"/></td>
									<td><xsl:value-of select="datetime"/></td>
									<td><xsl:value-of select="genre"/></td>
									<td><xsl:value-of select="performers"/></td>
									<td><xsl:value-of select="ticktype"/></td>
									<td><xsl:value-of select="seller"/></td>
									<td><xsl:value-of select="discount"/></td>
								</tr>
							</xsl:if>
							<xsl:if test="discount = 0">
								<tr>
									<td><xsl:value-of select="bind/name"/></td>
									<td><xsl:value-of select="bind/place"/></td>
									<td><xsl:value-of select="datetime"/></td>
									<td><xsl:value-of select="genre"/></td>
									<td><xsl:value-of select="performers"/></td>
									<td><xsl:value-of select="ticktype"/></td>
									<td><xsl:value-of select="seller"/></td>
								</tr>
							</xsl:if>
						</xsl:if>
					</xsl:for-each>
				</table>
			</body>
		</html>
	</xsl:template>

</xsl:stylesheet>
