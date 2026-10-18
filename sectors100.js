/**
 * 100 Official Sectors of Mumbai & Indian Administrative Zones
 * Reference dataset matching Reviewwflow v7a with Tier classifications,
 * GPS coordinates, landmarks, and 3D polygon bounding boxes.
 */

const MUMBAI_100_SECTORS = [
  {"id":"S001","name":"Bandra West","parent":"Bandra/Khar","landmarks":"Linking Rd, Pali Hill, Carter Rd, Bandstand, Waterfield Rd","tier":1,"lat":19.0596,"lon":72.8295},
  {"id":"S002","name":"Khar West","parent":"Bandra/Khar","landmarks":"Khar Danda Rd, 14th/15th/16th Rd, Linking Rd ext","tier":1,"lat":19.0788759,"lon":72.8320646},
  {"id":"S003","name":"Santacruz West","parent":"Bandra/Khar","landmarks":"Juhu Tara Rd, Linking Rd (Santacruz), SV Rd","tier":1,"lat":19.0844004,"lon":72.8372899},
  {"id":"S004","name":"Bandra East · BKC","parent":"Bandra/Khar","landmarks":"BKC, Kalanagar, Income Tax, MMRDA grounds","tier":1,"lat":19.0638693,"lon":72.8666148},
  {"id":"S005","name":"Bandra Station West","parent":"Bandra/Khar","landmarks":"Hill Rd, Bazaar Rd, St. Peter's, Station Rd","tier":1,"lat":19.0552109,"lon":72.8304474},
  {"id":"S006","name":"Juhu","parent":"Andheri West","landmarks":"Juhu Beach, JVPD, ISKCON, Juhu Koliwada","tier":1,"lat":19.1130692,"lon":72.8266734},
  {"id":"S007","name":"Veera Desai · Oshiwara","parent":"Andheri West","landmarks":"Veera Desai Rd, Oshiwara Garden, Andheri Sports Complex","tier":1,"lat":19.1344232,"lon":72.8353783},
  {"id":"S008","name":"Lokhandwala","parent":"Andheri West","landmarks":"Lokhandwala Complex, Back Rd, Green Acres","tier":1,"lat":19.1430985,"lon":72.8246055},
  {"id":"S009","name":"Fort · Kala Ghoda","parent":"South Mumbai","landmarks":"Horniman Circle, Kala Ghoda, DN Rd, Fountain","tier":1,"lat":18.9320095,"lon":72.8350198},
  {"id":"S010","name":"Ballard Estate","parent":"South Mumbai","landmarks":"Ballard Pier, Custom House, Fort south","tier":1,"lat":18.9366512,"lon":72.8391325},
  {"id":"S011","name":"Colaba","parent":"South Mumbai","landmarks":"Colaba Causeway, Gateway, Regal Circle, Colaba Market","tier":1,"lat":18.9230531,"lon":72.8316969},
  {"id":"S012","name":"Cuffe Parade","parent":"South Mumbai","landmarks":"Nariman Point, NCPA, Maker Chambers","tier":1,"lat":18.9251593,"lon":72.8205615},
  {"id":"S013","name":"Churchgate","parent":"South Mumbai","landmarks":"Marine Drive, Eros Cinema, Churchgate station","tier":1,"lat":18.9337168,"lon":72.8274613},
  {"id":"S014","name":"Malabar Hill","parent":"South Mumbai","landmarks":"Walkeshwar, Banganga, Teen Batti, Ridge Rd","tier":1,"lat":18.9581616,"lon":72.8033665},
  {"id":"S015","name":"Altamount Rd","parent":"South Mumbai","landmarks":"Altamount Rd, Carmichael Rd, Pedder Rd, Hughes Rd","tier":1,"lat":18.9730483,"lon":72.8101437},
  {"id":"S016","name":"Breach Candy","parent":"South Mumbai","landmarks":"Warden Rd, Mahalaxmi Temple, Amarsons, Bhulabhai Desai Rd","tier":1,"lat":18.9714363,"lon":72.8051492},
  {"id":"S017","name":"Dadar West","parent":"Dadar/Central","landmarks":"Ranade Rd, Shivaji Park, Plaza, NC Kelkar Rd","tier":1,"lat":19.0272788,"lon":72.8383977},
  {"id":"S018","name":"Prabhadevi","parent":"Dadar/Central","landmarks":"Siddhivinayak, Sayani Rd, Ravindra Natya Mandir","tier":1,"lat":19.0148811,"lon":72.8279556},
  {"id":"S019","name":"Worli","parent":"Dadar/Central","landmarks":"Worli Sea Face, Worli Village, Dr. Annie Besant Rd","tier":1,"lat":19.0086197,"lon":72.8146698},
  {"id":"S020","name":"Lower Parel","parent":"Dadar/Central","landmarks":"Phoenix Mills, High Street Phoenix, Mathuradas Mill","tier":1,"lat":18.9946688,"lon":72.8243102},
  {"id":"S021","name":"Powai","parent":"Powai/Andheri East","landmarks":"Hiranandani, Galleria, JVLR, IIT Main Gate","tier":1,"lat":19.1193993,"lon":72.9116357},
  {"id":"S022","name":"Vile Parle West","parent":"Bandra/Khar","landmarks":"Market Rd, Bajaj Rd, Sathaye College, station W","tier":1,"lat":19.0999098,"lon":72.8440038},
  {"id":"S023","name":"Mahalaxmi","parent":"South Mumbai","landmarks":"Racecourse, Haji Ali, Saat Rasta, Dr. E Moses Rd","tier":2,"lat":18.9852045,"lon":72.8205984},
  {"id":"S024","name":"Tardeo","parent":"South Mumbai","landmarks":"Opera House, Kennedy Bridge, Tardeo Rd","tier":2,"lat":18.9628835,"lon":72.813514},
  {"id":"S025","name":"Kalbadevi","parent":"South Mumbai","landmarks":"Zaveri Bazaar, Crawford Market, Bhuleshwar, Abdul Rehman St","tier":2,"lat":18.9492575,"lon":72.8279382},
  {"id":"S026","name":"Dadar East","parent":"Dadar/Central","landmarks":"Hindu Colony, Tilak Bridge, station E","tier":2,"lat":19.0199623,"lon":72.8478929},
  {"id":"S027","name":"Parel","parent":"Dadar/Central","landmarks":"Lalbaug, Currey Rd, KEM, Parel station","tier":2,"lat":19.0094817,"lon":72.8376614},
  {"id":"S028","name":"Matunga","parent":"Dadar/Central","landmarks":"King's Circle, Five Gardens, Matunga station","tier":2,"lat":19.0195374,"lon":72.8537881},
  {"id":"S029","name":"Mahim","parent":"Dadar/Central","landmarks":"Mori Rd, Mahim Causeway, Hinduja Hospital","tier":2,"lat":19.0406634,"lon":72.8466038},
  {"id":"S030","name":"Santacruz East · Kalina","parent":"Bandra/Khar","landmarks":"Kalina, Mumbai University, BKC fringe, CST Rd","tier":2,"lat":19.0734267,"lon":72.854825},
  {"id":"S031","name":"DN Nagar","parent":"Andheri West","landmarks":"Azad Nagar, JP Rd, DN Nagar metro, Sports Complex","tier":2,"lat":19.1278285,"lon":72.8308602},
  {"id":"S032","name":"Four Bungalows","parent":"Andheri West","landmarks":"Manish Nagar, RTO, Four Bungalows signal","tier":2,"lat":19.1287942,"lon":72.8255543},
  {"id":"S033","name":"Versova","parent":"Andheri West","landmarks":"Yari Rd, Versova Village, jetty, beach","tier":2,"lat":19.1300123,"lon":72.8133251},
  {"id":"S034","name":"Vile Parle East","parent":"Bandra/Khar","landmarks":"Sahar Rd, Nehru Rd, Parle Tilak, station E","tier":2,"lat":19.1097455,"lon":72.8365427},
  {"id":"S035","name":"Chandivali","parent":"Powai/Andheri East","landmarks":"Nahar Amrit Shakti, Chandivali Farm Rd","tier":2,"lat":19.1091482,"lon":72.8945793},
  {"id":"S036","name":"Chakala","parent":"Powai/Andheri East","landmarks":"JB Nagar, Andheri-Kurla Rd, WEH, Chakala metro","tier":2,"lat":19.1152873,"lon":72.8618085},
  {"id":"S037","name":"Sakinaka","parent":"Powai/Andheri East","landmarks":"90 Feet Rd, Khairani Rd, Sakinaka metro","tier":2,"lat":19.1006236,"lon":72.8805461},
  {"id":"S038","name":"Marol","parent":"Powai/Andheri East","landmarks":"Military Rd, Marol Naka, Marol Church","tier":2,"lat":19.1097535,"lon":72.8759757},
  {"id":"S039","name":"Andheri East Town","parent":"Powai/Andheri East","landmarks":"Telli Galli, Pump House, Gundavali, station E","tier":2,"lat":19.1205638,"lon":72.8488433},
  {"id":"S040","name":"Ghatkopar West","parent":"Ghatkopar/Vikhroli","landmarks":"MG Rd, station W, R City Mall","tier":2,"lat":19.0997411,"lon":72.915661},
  {"id":"S041","name":"Ghatkopar East","parent":"Ghatkopar/Vikhroli","landmarks":"Pant Nagar, Vikrant Circle, Tilak Rd","tier":2,"lat":19.0833305,"lon":72.9115042},
  {"id":"S042","name":"Malad West · Link Rd","parent":"Malad/Borivali","landmarks":"Link Rd, Inorbit, Mindspace","tier":2,"lat":19.1852851,"lon":72.8358611},
  {"id":"S043","name":"Orlem · Evershine","parent":"Malad/Borivali","landmarks":"Orlem, Evershine Nagar, Mith Chowki","tier":2,"lat":19.1823,"lon":72.8406},
  {"id":"S044","name":"Kandivali West","parent":"Malad/Borivali","landmarks":"MG Rd, station W, Shimpoli","tier":2,"lat":19.2041136,"lon":72.8517376},
  {"id":"S045","name":"Thakur Village","parent":"Malad/Borivali","landmarks":"Thakur Village, Thakur Complex, Lokhandwala Township","tier":2,"lat":19.2119479,"lon":72.8694449},
  {"id":"S046","name":"Borivali West","parent":"Malad/Borivali","landmarks":"Chandawarkar Ln, station W, IC Colony","tier":2,"lat":19.2298129,"lon":72.8471376},
  {"id":"S047","name":"Thane West · Naupada","parent":"Thane/Mulund","landmarks":"Naupada, station, Teen Hath Naka","tier":2,"lat":19.1888027,"lon":72.9633143},
  {"id":"S048","name":"Ghodbunder Rd","parent":"Thane/Mulund","landmarks":"Ghodbunder Rd, Hypercity, Waghbil","tier":2,"lat":19.2681,"lon":72.9677},
  {"id":"S049","name":"Hiranandani Estate","parent":"Thane/Mulund","landmarks":"Hiranandani Estate, Patlipada","tier":2,"lat":19.2549288,"lon":72.9820704},
  {"id":"S050","name":"Majiwada","parent":"Thane/Mulund","landmarks":"Viviana Mall, Jupiter Hospital, Eastern Express Hwy","tier":2,"lat":19.2089,"lon":72.9716},
  {"id":"S051","name":"Mulund West","parent":"Thane/Mulund","landmarks":"MG Rd, R Mall, station W","tier":2,"lat":19.1839747,"lon":72.9515934},
  {"id":"S052","name":"Vashi","parent":"Navi Mumbai","landmarks":"Sec 17 market, Inorbit Vashi, Palm Beach Rd","tier":2,"lat":19.0654352,"lon":73.0012477},
  {"id":"S053","name":"Nerul","parent":"Navi Mumbai","landmarks":"Sec 21, Seawoods Grand Central, Palm Beach","tier":2,"lat":19.0335938,"lon":73.018164},
  {"id":"S054","name":"Seawoods · Belapur CBD","parent":"Navi Mumbai","landmarks":"CBD Belapur, Sec 11, Seawoods station","tier":2,"lat":19.0205616,"lon":73.0180886},
  {"id":"S055","name":"Kharghar","parent":"Navi Mumbai","landmarks":"Golf Course, Central Park, Sec 12","tier":2,"lat":19.025773,"lon":73.0591845},
  {"id":"S056","name":"Chembur West","parent":"Dadar/Central","landmarks":"Station W, Diamond Garden, Chembur Naka","tier":2,"lat":19.0531279,"lon":72.9004824},
  {"id":"S057","name":"Kurla West","parent":"Dadar/Central","landmarks":"Station W, LBS Marg, Kamani","tier":2,"lat":19.0652797,"lon":72.8793805},
  {"id":"S058","name":"Jogeshwari West","parent":"Andheri West","landmarks":"Oshiwara station, Behram Baug, JVLR","tier":2,"lat":19.135,"lon":72.845},
  {"id":"S059","name":"Goregaon West","parent":"Malad/Borivali","landmarks":"MG Rd, Bangur Nagar, station W, Aarey Rd","tier":2,"lat":19.1648688,"lon":72.8495492},
  {"id":"S060","name":"Goregaon East","parent":"Malad/Borivali","landmarks":"Oberoi Mall, Commerz, Nirlon, JVLR","tier":2,"lat":19.1737223,"lon":72.8606297},
  {"id":"S061","name":"Chembur East","parent":"Dadar/Central","landmarks":"Sindhi Camp, Trombay Rd, station E","tier":2,"lat":19.0734855,"lon":72.8823214},
  {"id":"S062","name":"Airoli","parent":"Navi Mumbai","landmarks":"Sec 19, Mindspace, station, Thane-Belapur Rd","tier":2,"lat":19.161493,"lon":73.0021466},
  {"id":"S063","name":"Mumbai Central","parent":"South Mumbai","landmarks":"Agripada, Madanpura, Maratha Mandir, station","tier":3,"lat":18.9695855,"lon":72.8193152},
  {"id":"S064","name":"Byculla","parent":"South Mumbai","landmarks":"Mazgaon, Dockyard Rd, Gloria Church, station","tier":3,"lat":18.9764065,"lon":72.8327044},
  {"id":"S065","name":"Dongri","parent":"South Mumbai","landmarks":"Bhendi Bazaar, Umerkhadi","tier":3,"lat":18.9579427,"lon":72.8317816},
  {"id":"S066","name":"Sion","parent":"Dadar/Central","landmarks":"GTB Nagar, Sion Circle, Sion Hospital","tier":3,"lat":19.0427327,"lon":72.863491},
  {"id":"S067","name":"Wadala","parent":"Dadar/Central","landmarks":"Bhakti Park, IMAX, Wadala station","tier":3,"lat":19.0269192,"lon":72.8759337},
  {"id":"S068","name":"Kurla East","parent":"Dadar/Central","landmarks":"Nehru Nagar, station E","tier":3,"lat":19.061,"lon":72.881},
  {"id":"S069","name":"Govandi","parent":"Dadar/Central","landmarks":"Deonar, Baiganwadi, station","tier":3,"lat":19.0553688,"lon":72.9150702},
  {"id":"S070","name":"Tilak Nagar","parent":"Dadar/Central","landmarks":"Tilak Nagar station, Pestom Sagar, Chembur border","tier":3,"lat":19.0657855,"lon":72.8904702},
  {"id":"S071","name":"Khar East · Vakola","parent":"Bandra/Khar","landmarks":"Khar East, Vakola, Prabhat Colony","tier":3,"lat":19.0833,"lon":72.845},
  {"id":"S072","name":"Jogeshwari East","parent":"Powai/Andheri East","landmarks":"JVLR, Majas, station E, WEH","tier":3,"lat":19.135,"lon":72.867},
  {"id":"S073","name":"MIDC · Seepz","parent":"Powai/Andheri East","landmarks":"Seepz Gate, MIDC Central Rd","tier":3,"lat":19.1056,"lon":72.8623},
  {"id":"S074","name":"Kanjurmarg West","parent":"Powai/Andheri East","landmarks":"LBS Marg, IIT boundary, station W","tier":3,"lat":19.1253912,"lon":72.9252519},
  {"id":"S075","name":"Vikhroli East","parent":"Ghatkopar/Vikhroli","landmarks":"Kannamwar Nagar, Tagore Nagar, station E","tier":3,"lat":19.1164674,"lon":72.9356821},
  {"id":"S076","name":"Vikhroli West","parent":"Ghatkopar/Vikhroli","landmarks":"Godrej, station W, LBS Marg","tier":3,"lat":19.1114795,"lon":72.928021},
  {"id":"S077","name":"Bhandup West","parent":"Ghatkopar/Vikhroli","landmarks":"LBS Marg, station W, Dreams Mall","tier":3,"lat":19.145916,"lon":72.9366395},
  {"id":"S078","name":"Bhandup East · Nahur","parent":"Ghatkopar/Vikhroli","landmarks":"Nahur station, Tank Rd","tier":3,"lat":19.1546144,"lon":72.9467761},
  {"id":"S079","name":"Kanjurmarg East","parent":"Ghatkopar/Vikhroli","landmarks":"Station E, LBS Marg","tier":3,"lat":19.124102,"lon":72.9385562},
  {"id":"S080","name":"Asalpha · Saki Vihar","parent":"Ghatkopar/Vikhroli","landmarks":"Asalpha, Saki Vihar Rd","tier":3,"lat":19.1028484,"lon":72.8862483},
  {"id":"S081","name":"Malad East · Kurar","parent":"Malad/Borivali","landmarks":"Kurar, Dindoshi, Pathanwadi","tier":3,"lat":19.1867,"lon":72.8611},
  {"id":"S082","name":"Charkop","parent":"Malad/Borivali","landmarks":"Charkop market, Sector 8","tier":3,"lat":19.2141193,"lon":72.8258652},
  {"id":"S083","name":"Borivali East","parent":"Malad/Borivali","landmarks":"Station E, SGNP Rd, Kastur Park","tier":3,"lat":19.229068,"lon":72.8573628},
  {"id":"S084","name":"Eksar · Mandpeshwar","parent":"Malad/Borivali","landmarks":"Eksar, Mandpeshwar, Yogi Nagar","tier":3,"lat":19.2307,"lon":72.8448},
  {"id":"S085","name":"Dahisar West","parent":"Malad/Borivali","landmarks":"Station W, Anand Nagar, SV Rd","tier":3,"lat":19.248875,"lon":72.852959},
  {"id":"S086","name":"Dahisar East","parent":"Malad/Borivali","landmarks":"SV Rd, Rawal Pada, station E","tier":3,"lat":19.2493572,"lon":72.8596302},
  {"id":"S087","name":"Mira Rd West","parent":"Malad/Borivali","landmarks":"Station W, Silver Park, Shanti Nagar","tier":3,"lat":19.2791,"lon":72.851},
  {"id":"S088","name":"Mira Rd East","parent":"Malad/Borivali","landmarks":"Vinay Nagar, Shanti Park, station E","tier":3,"lat":19.2791,"lon":72.862},
  {"id":"S089","name":"Bhayandar West","parent":"Malad/Borivali","landmarks":"Station W, Jesal Park","tier":3,"lat":19.2952,"lon":72.849},
  {"id":"S090","name":"Bhayandar East","parent":"Malad/Borivali","landmarks":"Goddev, Fatak Rd, station E","tier":3,"lat":19.2952,"lon":72.86},
  {"id":"S091","name":"Wagle Estate","parent":"Thane/Mulund","landmarks":"Wagle Estate, Kopri, Thane East","tier":3,"lat":19.1985175,"lon":72.9509778},
  {"id":"S092","name":"Vartak Nagar","parent":"Thane/Mulund","landmarks":"Pokhran Rd, Vartak Nagar","tier":3,"lat":19.2115972,"lon":72.9616225},
  {"id":"S093","name":"Kolshet Rd","parent":"Thane/Mulund","landmarks":"Kolshet, Dhokali","tier":3,"lat":19.2290562,"lon":72.9836731},
  {"id":"S094","name":"Kasarvadavali","parent":"Thane/Mulund","landmarks":"Ghodbunder far, Kasarvadavali naka","tier":3,"lat":19.2704158,"lon":72.969082},
  {"id":"S095","name":"Mulund East","parent":"Thane/Mulund","landmarks":"Station E, Nahur border, LBS Marg","tier":3,"lat":19.1721366,"lon":72.9566971},
  {"id":"S096","name":"Koparkhairane","parent":"Navi Mumbai","landmarks":"Sec 11, station, Thane-Belapur Rd","tier":3,"lat":19.1055907,"lon":72.9982312},
  {"id":"S097","name":"Ghansoli","parent":"Navi Mumbai","landmarks":"Talavali, station","tier":3,"lat":19.1165736,"lon":73.0050498},
  {"id":"S098","name":"Sanpada · Juinagar","parent":"Navi Mumbai","landmarks":"Sanpada station, Juinagar, Palm Beach","tier":3,"lat":19.0669987,"lon":73.0092292},
  {"id":"S099","name":"Panvel","parent":"Navi Mumbai","landmarks":"Station, Old Panvel, ST stand","tier":3,"lat":18.9986,"lon":73.1114},
  {"id":"S100","name":"Kamothe · Kalamboli","parent":"Navi Mumbai","landmarks":"Kamothe, Kalamboli, Sion-Panvel Hwy","tier":3,"lat":19.0164338,"lon":73.0806552}
];

function getSectorPolygonBounds(lat, lon, delta = 0.009) {
    return [
        { lat: lat - delta, lng: lon - delta * 1.05 },
        { lat: lat + delta, lng: lon - delta * 1.05 },
        { lat: lat + delta, lng: lon + delta * 1.05 },
        { lat: lat - delta, lng: lon + delta * 1.05 }
    ];
}

const INDIAN_STATES_AND_REGIONS = {
    "mumbai_100": {
        name: "Mumbai (100 Sectors - T1/T2/T3)",
        type: "district",
        center: { lat: 19.0760, lng: 72.8777 },
        zoom: 12,
        tilt: 62,
        heading: 15,
        sectors: MUMBAI_100_SECTORS.map((s, idx) => ({
            id: s.id,
            index: idx + 1,
            name: `${s.id} · ${s.name}`,
            locality: s.name,
            parent: s.parent,
            landmarks: s.landmarks,
            tier: s.tier,
            center: { lat: s.lat, lng: s.lon },
            polygon: getSectorPolygonBounds(s.lat, s.lon, 0.008),
            bounds: {
                south: s.lat - 0.008,
                north: s.lat + 0.008,
                west: s.lon - 0.008,
                east: s.lon + 0.008
            },
            camera_3d: {
                center: { lat: s.lat, lng: s.lon },
                tilt: 62,
                heading: (idx * 25) % 360,
                zoom: 16
            }
        }))
    },
    "delhi_ncr": {
        name: "Delhi NCR (64 Sectors)",
        type: "district",
        center: { lat: 28.6139, lng: 77.2090 },
        bounds: [28.4500, 76.9500, 28.8500, 77.3500],
        zoom: 12,
        tilt: 60,
        heading: 0,
        grid: [8, 8]
    },
    "bengaluru": {
        name: "Bengaluru Urban (64 Sectors)",
        type: "district",
        center: { lat: 12.9716, lng: 77.5946 },
        bounds: [12.8500, 77.4800, 13.1200, 77.7500],
        zoom: 12,
        tilt: 60,
        heading: 15,
        grid: [8, 8]
    },
    "pune": {
        name: "Pune City (36 Sectors)",
        type: "district",
        center: { lat: 18.5204, lng: 73.8567 },
        bounds: [18.4400, 73.7600, 18.6100, 73.9600],
        zoom: 12,
        tilt: 55,
        heading: 10,
        grid: [6, 6]
    },
    "hyderabad": {
        name: "Hyderabad (36 Sectors)",
        type: "district",
        center: { lat: 17.3850, lng: 78.4867 },
        bounds: [17.3000, 78.3300, 17.5200, 78.5800],
        zoom: 12,
        tilt: 55,
        heading: 0,
        grid: [6, 6]
    },
    "maharashtra": {
        name: "Maharashtra State (64 Grid Zones)",
        type: "state",
        center: { lat: 19.7515, lng: 75.7139 },
        bounds: [15.6000, 72.6000, 22.0000, 80.9000],
        zoom: 7,
        tilt: 45,
        heading: 0,
        grid: [8, 8]
    },
    "karnataka": {
        name: "Karnataka State (64 Grid Zones)",
        type: "state",
        center: { lat: 15.3173, lng: 75.7139 },
        bounds: [11.5000, 74.0000, 18.5000, 78.6000],
        zoom: 7,
        tilt: 45,
        heading: 0,
        grid: [8, 8]
    },
    "gujarat": {
        name: "Gujarat State (64 Grid Zones)",
        type: "state",
        center: { lat: 22.2587, lng: 71.1924 },
        bounds: [20.1000, 68.1000, 24.7000, 74.5000],
        zoom: 7,
        tilt: 45,
        heading: 0,
        grid: [8, 8]
    },
    "tamil_nadu": {
        name: "Tamil Nadu State (64 Grid Zones)",
        type: "state",
        center: { lat: 11.1271, lng: 78.6569 },
        bounds: [8.0500, 76.2000, 13.5500, 80.3500],
        zoom: 7,
        tilt: 45,
        heading: 0,
        grid: [8, 8]
    }
};

function generateDynamicGrid(regionKey) {
    const r = INDIAN_STATES_AND_REGIONS[regionKey];
    if (!r) return INDIAN_STATES_AND_REGIONS["mumbai_100"].sectors;
    if (r.sectors) return r.sectors;

    const [south, west, north, east] = r.bounds;
    const [rows, cols] = r.grid || [8, 8];
    const latStep = (north - south) / rows;
    const lngStep = (east - west) / cols;
    const sectors = [];
    let idx = 1;

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const sLat = south + row * latStep;
            const nLat = south + (row + 1) * latStep;
            const wLng = west + col * lngStep;
            const eLng = west + (col + 1) * lngStep;
            const cLat = (sLat + nLat) / 2;
            const cLng = (wLng + eLng) / 2;
            const secId = `Z${String(idx).padStart(3, '0')}`;

            sectors.push({
                id: secId,
                index: idx,
                name: `${secId} · ${r.name.split(' ')[0]} Sector ${idx}`,
                locality: `${r.name.split(' ')[0]} Zone ${row + 1}-${col + 1}`,
                parent: r.name,
                landmarks: `Lat: ${cLat.toFixed(3)}, Lng: ${cLng.toFixed(3)}`,
                tier: (row + col) % 3 + 1,
                center: { lat: cLat, lng: cLng },
                polygon: [
                    { lat: sLat, lng: wLng },
                    { lat: nLat, lng: wLng },
                    { lat: nLat, lng: eLng },
                    { lat: sLat, lng: eLng }
                ],
                bounds: { south: sLat, west: wLng, north: nLat, east: eLng },
                camera_3d: {
                    center: { lat: cLat, lng: cLng },
                    tilt: r.tilt || 55,
                    heading: 15,
                    zoom: 14
                }
            });
            idx++;
        }
    }
    return sectors;
}

window.MUMBAI_100_SECTORS = MUMBAI_100_SECTORS;
window.INDIAN_STATES_AND_REGIONS = INDIAN_STATES_AND_REGIONS;
window.generateDynamicGrid = generateDynamicGrid;
