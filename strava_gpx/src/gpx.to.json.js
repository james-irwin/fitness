var fs = require('fs');
var xml2js = require('xml2js');

// Changes XML to JSON
function xmlToJson(xml) {

    // Create the return object
    var obj = {};

    if (xml.nodeType == 1) { // element
        // do attributes
        if (xml.attributes.length > 0) {
            obj["@attributes"] = {};
            for (var j = 0; j < xml.attributes.length; j++) {
                var attribute = xml.attributes.item(j);
                obj["@attributes"][attribute.nodeName] = attribute.nodeValue;
            }
        }
    } else if (xml.nodeType == 3) { // text
        obj = xml.nodeValue;
    }

    // do children
    if (xml.hasChildNodes()) {
        for (var i = 0; i < xml.childNodes.length; i++) {
            var item = xml.childNodes.item(i);
            var nodeName = item.nodeName;
            if (typeof (obj[nodeName]) == "undefined") {
                obj[nodeName] = xmlToJson(item);
            } else {
                if (typeof (obj[nodeName].push) == "undefined") {
                    var old = obj[nodeName];
                    obj[nodeName] = [];
                    obj[nodeName].push(old);
                }
                obj[nodeName].push(xmlToJson(item));
            }
        }
    }
    return obj;
};

function replaceAll(find, replace, str) {
    var mystr=String(str);
    return mystr.replace(new RegExp(find, 'g'), replace);
}

function twist(err, data) {
    if (err) throw err;

    var parser = xml2js.Parser();
    parser.parseString(data, function (err, result) {
	var whole_track = result['gpx']['trk'];
	for (track_id in whole_track)
	{
		var track = whole_track[track_id];
		for (segment_id in track['trkseg'])
		{
			var segment = track['trkseg'][segment_id];
			for (point_id in segment['trkpt'])
			{
				var rec = {};
				var src = segment['trkpt'][point_id];
				rec.timestamp       = src.time[0];
				rec.position        = {};
				rec.position.lat    = src['$']['lat']*1;
				rec.position.lon    = src['$']['lon']*1;
				rec.altitude        = Math.round(src['ele']*100);
				rec.heart_rate      = Math.round(src['extensions'][0]['gpxtpx:TrackPointExtension'][0]['gpxtpx:hr'][0]);
				console.log(JSON.stringify(rec));
			}
		}
	}
	}
                      );
}

var data = fs.readFile(process.argv[2], twist);
