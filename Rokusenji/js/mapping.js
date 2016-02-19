    //<![CDATA[
function mapping() {
	var map = new GMap2(document.getElementById("map"));
	var latlng  = new GLatLng(33.539301, 133.541625);
	
	var infoTabs = [
		new GInfoWindowTab("医院情報",
			"<h3>六泉寺歯科</h3>" +
			"<p>〒780-8023　高知市六泉寺町15-13</p>" +
			"<p><a href='http://www.rokusenji-sika.com/'>http://www.rokusenji-sika.com/</a></p>"),
		new GInfoWindowTab("アクセス",
			"<ul><li>土佐電鉄バス　六泉寺停留所前</li><li>県交通バス　六泉寺停留所下車徒歩1分</li><li>サニーマート六泉寺店向かいになります</li></ul>")
	];

	map.setCenter(latlng, 15);
	
	map.addControl(new GSmallMapControl());
	map.addControl(new GMapTypeControl());

	var marker = new GMarker(latlng);
	map.addOverlay(marker);
	
	GEvent.addListener(marker, "click", function() {
		marker.openInfoWindowTabsHtml(infoTabs);
	});
	
}
//]]>
