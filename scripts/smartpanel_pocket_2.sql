--
-- PostgreSQL database insert of Pocket widget configs 

--
-- Data for Name: smartpanel_pocket; Type: TABLE DATA; Schema: public; Owner: tfc_prod
--

INSERT INTO smartpanel_pocket (name, params)
SELECT
'1','[{"data": {"stop": {"id": "0500CCITY424", "lat": 52.2112996707, "lng": 0.09107756159, "stop_id": "0500CCITY424", "latitude": 52.2112996707, "atco_code": "0500CCITY424", "indicator": "opp", "longitude": 0.09107756159, "common_name": "William Gates Building", "naptan_code": "CMBDGDMT", "locality_name": "Cambridge"}, "title": "Opposite William Gates Building", "layout": "multiline", "destinations": [{"area": [{"lat": 52.17570364175672, "lng": 0.14228330925107005}, {"lat": 52.175488800588674, "lng": 0.1444551441818476}, {"lat": 52.176017346023265, "lng": 0.14606296084821227}, {"lat": 52.17649558019505, "lng": 0.14505780301988128}, {"lat": 52.17622663512504, "lng": 0.14254231005907061}], "description": "Hospital"}, {"area": [{"lat": 52.205272570950065, "lng": 0.12231070082634689}, {"lat": 52.20584108642862, "lng": 0.12381173204630615}, {"lat": 52.20498217848623, "lng": 0.12558894697576764}, {"lat": 52.20354579109039, "lng": 0.12294583953917028}, {"lat": 52.204710238021654, "lng": 0.12170623987913133}], "description": "City Centre"}, {"area": [{"lat": 52.32328491326036, "lng": -0.07158505730330945}, {"lat": 52.3232474380255, "lng": -0.07017082069069148}, {"lat": 52.322305705435205, "lng": -0.07021650206297637}, {"lat": 52.32234784355564, "lng": -0.07179640699177982}], "description": "St Ives Bus Station"}, {"area": [{"lat": 52.19371446386684, "lng": 0.1361500192433596}, {"lat": 52.19349174821103, "lng": 0.1370208151638508}, {"lat": 52.1922004274234, "lng": 0.13610429596155885}, {"lat": 52.19241752500701, "lng": 0.1352344220504165}], "description": "Station"}]}, "title": "Opposite William Gates Building", "widget": "stop_timetable"}, {"data": {"station": "CBG", "platforms": "y"}, "title": "Cambridge", "widget": "station_board"}, {"data": {"location": "310042"}, "title": "Cambridge", "widget": "weather"}]'
WHERE NOT EXISTS (
    SELECT name FROM smartpanel_pocket WHERE name = '1'
);


INSERT INTO smartpanel_pocket (name, params)
SELECT
'2','[{"data": {"stop": {"id": "0500CCITY474", "lat": 52.2099970222, "lng": 0.09050408588, "stop_id": "0500CCITY474", "latitude": 52.2099970222, "atco_code": "0500CCITY474", "indicator": "opp", "longitude": 0.09050408588, "common_name": "Cavendish Laboratory", "naptan_code": "CMBGJGTA", "locality_name": "Cambridge"}, "title": "Opposite Cavendish Laboratory", "layout": "multiline", "destinations": [{"area": [{"lat": 52.17570364175672, "lng": 0.14228330925107005}, {"lat": 52.175488800588674, "lng": 0.1444551441818476}, {"lat": 52.176017346023265, "lng": 0.14606296084821227}, {"lat": 52.17649558019505, "lng": 0.14505780301988128}, {"lat": 52.17622663512504, "lng": 0.14254231005907061}], "description": "Hospital"}, {"area": [{"lat": 52.205272570950065, "lng": 0.12231070082634689}, {"lat": 52.20584108642862, "lng": 0.12381173204630615}, {"lat": 52.20498217848623, "lng": 0.12558894697576764}, {"lat": 52.20354579109039, "lng": 0.12294583953917028}, {"lat": 52.204710238021654, "lng": 0.12170623987913133}], "description": "City Centre"}, {"area": [{"lat": 52.32328491326036, "lng": -0.07158505730330945}, {"lat": 52.3232474380255, "lng": -0.07017082069069148}, {"lat": 52.322305705435205, "lng": -0.07021650206297637}, {"lat": 52.32234784355564, "lng": -0.07179640699177982}], "description": "St Ives Bus Station"}, {"area": [{"lat": 52.19371446386684, "lng": 0.1361500192433596}, {"lat": 52.19349174821103, "lng": 0.1370208151638508}, {"lat": 52.1922004274234, "lng": 0.13610429596155885}, {"lat": 52.19241752500701, "lng": 0.1352344220504165}], "description": "Station"}]}, "title": "Opposite Cavendish Laboratory", "widget": "stop_timetable"}, {"data": {"station": "CBG", "platforms": "y"}, "title": "Cambridge", "widget": "station_board"}, {"data": {"location": "310042"}, "title": "Cambridge", "widget": "weather"}]'
WHERE NOT EXISTS (
    SELECT name FROM smartpanel_pocket WHERE name = '2'
);

INSERT INTO smartpanel_pocket (name, params)
SELECT
'3','[{"data": {"stop": {"id": "0500CCITY521", "lat": 52.2098578112, "lng": 0.08770187421, "stop_id": "0500CCITY521", "latitude": 52.2098578112, "atco_code": "0500CCITY521", "indicator": "near", "longitude": 0.08770187421, "common_name": "Veterinary School", "naptan_code": "CMBGMATD", "locality_name": "Cambridge"}, "title": "Near Veterinary School", "layout": "multiline", "destinations": [{"area": [{"lat": 52.17570364175672, "lng": 0.14228330925107005}, {"lat": 52.175488800588674, "lng": 0.1444551441818476}, {"lat": 52.176017346023265, "lng": 0.14606296084821227}, {"lat": 52.17649558019505, "lng": 0.14505780301988128}, {"lat": 52.17622663512504, "lng": 0.14254231005907061}], "description": "Hospital"}, {"area": [{"lat": 52.205272570950065, "lng": 0.12231070082634689}, {"lat": 52.20584108642862, "lng": 0.12381173204630615}, {"lat": 52.20498217848623, "lng": 0.12558894697576764}, {"lat": 52.20354579109039, "lng": 0.12294583953917028}, {"lat": 52.204710238021654, "lng": 0.12170623987913133}], "description": "City Centre"}, {"area": [{"lat": 52.32328491326036, "lng": -0.07158505730330945}, {"lat": 52.3232474380255, "lng": -0.07017082069069148}, {"lat": 52.322305705435205, "lng": -0.07021650206297637}, {"lat": 52.32234784355564, "lng": -0.07179640699177982}], "description": "St Ives Bus Station"}, {"area": [{"lat": 52.19371446386684, "lng": 0.1361500192433596}, {"lat": 52.19349174821103, "lng": 0.1370208151638508}, {"lat": 52.1922004274234, "lng": 0.13610429596155885}, {"lat": 52.19241752500701, "lng": 0.1352344220504165}], "description": "Station"}]}, "title": "Near Veterinary School", "widget": "stop_timetable"}, {"data": {"station": "CBG", "platforms": "y"}, "title": "Cambridge", "widget": "station_board"}, {"data": {"location": "310042"}, "title": "Cambridge", "widget": "weather"}]'
WHERE NOT EXISTS (
    SELECT name FROM smartpanel_pocket WHERE name = '3'
);

INSERT INTO smartpanel_pocket (name, params)
SELECT
'4','['
'{"widget":"stop_timetable","title":"Opp. Shire Hall 5 & 6","data":{"stop":{"id":"0500CCITY401","stop_id":"0500CCITY401","atco_code":"0500CCITY401","naptan_code":"CMBDGDAP","common_name":"Shire Hall","indicator":"opp","locality_name":"Cambridge","latitude":52.2129798317,"longitude":0.11235244692,"lat":52.2129798317,"lng":0.11235244692},"title":"Opp. Shire Hall 5 & 6","layout":"multiline","destinations":[{"area":[{"lat":52.17570364175672,"lng":0.14228330925107005},{"lat":52.175488800588674,"lng":0.1444551441818476},{"lat":52.176017346023265,"lng":0.14606296084821227},{"lat":52.17649558019505,"lng":0.14505780301988128},{"lat":52.17622663512504,"lng":0.14254231005907061}],"description":"Hospital"},{"area":[{"lat":52.205272570950065,"lng":0.12231070082634689},{"lat":52.20584108642862,"lng":0.12381173204630615},{"lat":52.20498217848623,"lng":0.12558894697576764},{"lat":52.20354579109039,"lng":0.12294583953917028},{"lat":52.204710238021654,"lng":0.12170623987913133}],"description":"City Centre"},{"area":[{"lat":52.32328491326036,"lng":-0.07158505730330945},{"lat":52.3232474380255,"lng":-0.07017082069069148},{"lat":52.322305705435205,"lng":-0.07021650206297637},{"lat":52.32234784355564,"lng":-0.07179640699177982}],"description":"St Ives Bus Station"},{"area":[{"lat":52.19371446386684,"lng":0.1361500192433596},{"lat":52.19349174821103,"lng":0.1370208151638508},{"lat":52.1922004274234,"lng":0.13610429596155885},{"lat":52.19241752500701,"lng":0.1352344220504165}],"description":"Station"}]}},'
'{"widget":"stop_timetable","title":"Opp. Shire Hall Busway B","data":{"stop":{"id":"0500CCITY497","stop_id":"0500CCITY497","atco_code":"0500CCITY497","naptan_code":"CMBGJTMG","common_name":"The Busway Shire Hall","indicator":"opp","locality_name":"Cambridge","latitude":52.212749988,"longitude":0.11263430266,"lat":52.212749988,"lng":0.11263430266},"title":"Opp. Shire Hall Busway B","layout":"multiline","destinations":[{"area":[{"lat":52.17570364175672,"lng":0.14228330925107005},{"lat":52.175488800588674,"lng":0.1444551441818476},{"lat":52.176017346023265,"lng":0.14606296084821227},{"lat":52.17649558019505,"lng":0.14505780301988128},{"lat":52.17622663512504,"lng":0.14254231005907061}],"description":"Hospital","box":{"north":52.17649558019505,"south":52.175488800588674,"east":0.14606296084821227,"west":0.14228330925107005}},{"area":[{"lat":52.205272570950065,"lng":0.12231070082634689},{"lat":52.20584108642862,"lng":0.12381173204630615},{"lat":52.20498217848623,"lng":0.12558894697576764},{"lat":52.20354579109039,"lng":0.12294583953917028},{"lat":52.204710238021654,"lng":0.12170623987913133}],"description":"City Centre","box":{"north":52.20584108642862,"south":52.20354579109039,"east":0.12558894697576764,"west":0.12170623987913133}},{"area":[{"lat":52.32328491326036,"lng":-0.07158505730330945},{"lat":52.3232474380255,"lng":-0.07017082069069148},{"lat":52.322305705435205,"lng":-0.07021650206297637},{"lat":52.32234784355564,"lng":-0.07179640699177982}],"description":"St Ives Bus Station","box":{"north":52.32328491326036,"south":52.322305705435205,"east":-0.07017082069069148,"west":-0.07179640699177982}},{"area":[{"lat":52.19371446386684,"lng":0.1361500192433596},{"lat":52.19349174821103,"lng":0.1370208151638508},{"lat":52.1922004274234,"lng":0.13610429596155885},{"lat":52.19241752500701,"lng":0.1352344220504165}],"description":"Station","box":{"north":52.19371446386684,"south":52.1922004274234,"east":0.1370208151638508,"west":0.1352344220504165}}]}},'
'{"title":"Cambridge Trains","data":{"station":"CBG","platforms":"y"},"widget":"station_board"},'
'{"title":"Cambridge Weather","data":{"location":"310042"},"widget":"weather"}'
']'
WHERE NOT EXISTS (
    SELECT name FROM smartpanel_pocket WHERE name = '4'
);

INSERT INTO smartpanel_pocket (name, params)
SELECT
'5','['
'{"widget":"stop_timetable","title":"Shire Hall to City 5 & 6","data":{"stop":{"id":"0500CCITY394","stop_id":"0500CCITY394","atco_code":"0500CCITY394","naptan_code":"CMBDGAWM","common_name":"Shire Hall","indicator":"o/s","locality_name":"Cambridge","latitude":52.2129748562,"longitude":0.11263033523,"lat":52.2129748562,"lng":0.11263033523},"title":"Shire Hall to City 5 & 6","layout":"multiline","destinations":[{"area":[{"lat":52.17570364175672,"lng":0.14228330925107005},{"lat":52.175488800588674,"lng":0.1444551441818476},{"lat":52.176017346023265,"lng":0.14606296084821227},{"lat":52.17649558019505,"lng":0.14505780301988128},{"lat":52.17622663512504,"lng":0.14254231005907061}],"description":"Hospital"},{"area":[{"lat":52.205272570950065,"lng":0.12231070082634689},{"lat":52.20584108642862,"lng":0.12381173204630615},{"lat":52.20498217848623,"lng":0.12558894697576764},{"lat":52.20354579109039,"lng":0.12294583953917028},{"lat":52.204710238021654,"lng":0.12170623987913133}],"description":"City Centre"},{"area":[{"lat":52.32328491326036,"lng":-0.07158505730330945},{"lat":52.3232474380255,"lng":-0.07017082069069148},{"lat":52.322305705435205,"lng":-0.07021650206297637},{"lat":52.32234784355564,"lng":-0.07179640699177982}],"description":"St Ives Bus Station"},{"area":[{"lat":52.19371446386684,"lng":0.1361500192433596},{"lat":52.19349174821103,"lng":0.1370208151638508},{"lat":52.1922004274234,"lng":0.13610429596155885},{"lat":52.19241752500701,"lng":0.1352344220504165}],"description":"Station"}]}},'
'{"widget":"stop_timetable","title":"Shire Hall to City Busway B","data":{"stop":{"id":"0500CCITY496","stop_id":"0500CCITY496","atco_code":"0500CCITY496","naptan_code":"CMBGJTMD","common_name":"The Busway Shire Hall","indicator":"o/s","locality_name":"Cambridge","latitude":52.2130028564,"longitude":0.11257311139,"lat":52.2130028564,"lng":0.11257311139},"title":"Shire Hall to City Busway B","layout":"multiline","destinations":[{"area":[{"lat":52.17570364175672,"lng":0.14228330925107005},{"lat":52.175488800588674,"lng":0.1444551441818476},{"lat":52.176017346023265,"lng":0.14606296084821227},{"lat":52.17649558019505,"lng":0.14505780301988128},{"lat":52.17622663512504,"lng":0.14254231005907061}],"description":"Hospital"},{"area":[{"lat":52.205272570950065,"lng":0.12231070082634689},{"lat":52.20584108642862,"lng":0.12381173204630615},{"lat":52.20498217848623,"lng":0.12558894697576764},{"lat":52.20354579109039,"lng":0.12294583953917028},{"lat":52.204710238021654,"lng":0.12170623987913133}],"description":"City Centre"},{"area":[{"lat":52.32328491326036,"lng":-0.07158505730330945},{"lat":52.3232474380255,"lng":-0.07017082069069148},{"lat":52.322305705435205,"lng":-0.07021650206297637},{"lat":52.32234784355564,"lng":-0.07179640699177982}],"description":"St Ives Bus Station"},{"area":[{"lat":52.19371446386684,"lng":0.1361500192433596},{"lat":52.19349174821103,"lng":0.1370208151638508},{"lat":52.1922004274234,"lng":0.13610429596155885},{"lat":52.19241752500701,"lng":0.1352344220504165}],"description":"Station"}]}},'
'{"title":"Cambridge Trains","data":{"station":"CBG","platforms":"y"},"widget":"station_board"},'
'{"title":"Cambridge Weather","data":{"location":"310042"},"widget":"weather"}'
']'
WHERE NOT EXISTS (
    SELECT name FROM smartpanel_pocket WHERE name = '5'
);

-- PostgreSQL database dump complete
--

