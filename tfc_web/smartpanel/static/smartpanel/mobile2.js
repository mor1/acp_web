/* globals ons, Weather, StationBoard, StopTimetable, StopBusMap, WIDGET_CONFIG, RTMonitorAPI */

'use strict';

var RTMONITOR_API;

const TCS_VERSION = 1;

const STORAGE = window.localStorage;

let PANELS = [];

ons.ready(function () {

    console.log('Running ready()');

    // Retrieve the configuration
    if (STORAGE.getItem('MOBILE_PANELS')) {
        PANELS = JSON.parse(STORAGE.getItem('MOBILE_PANELS'));
    }

    // Opening page depends in STORAGE.TCS_VERSION
    let raw_version = STORAGE.getItem('TCS_VERSION');
    if (raw_version && parseInt(raw_version) >= TCS_VERSION) {
        document.querySelector('#myNavigator').pushPage('panels.html');
    }
    else {
        document.querySelector('#myNavigator').pushPage('first.html');
    }

});


document.addEventListener('init', function(event) {
    var page = event.target;

    console.log(`Running init for ${page.id}`);

    if (page.id === 'first') {
        page.querySelector('#accept').addEventListener('click', function() {
            STORAGE.setItem('TCS_VERSION', TCS_VERSION.toString());
            document.querySelector('#myNavigator').pushPage('panels.html');
        });
    }

    else if (page.id === 'panels') {
        page.querySelector('#edit').addEventListener('click', function() {
            document.querySelector('#myNavigator').pushPage('panels-edit.html');
        });
        page.querySelector('#add').addEventListener('click', function() {
            document.querySelector('#myNavigator').pushPage('config.html');
        });
        page.querySelector('.panel-items').addEventListener('click', function(evt) {
            let list_item = evt.target.closest('ons-list-item');
            if (!list_item) {
                return;
            }
            let panel_number = getElementIndex(list_item);
            document.querySelector('#myNavigator').pushPage('panel.html', {data: { panel_number }});
        });
        populate_panel_list(page, false);
    }

    else if (page.id === 'panels-edit') {
        page.querySelector('#done').addEventListener('click', function() {
            document.querySelector('#myNavigator').popPage();
        });
        page.querySelector('.panel-items').addEventListener('click', function(evt) {
            let list_item = evt.target.closest('ons-list-item');
            if (!list_item) {
                return;
            }
            let panel_number = getElementIndex(list_item);
            if (evt.target.classList.contains('item-edit')) {
                console.log(`Edit ${panel_number}`);
            }
            else if (evt.target.classList.contains('item-delete')) {
                console.log(`Delete ${panel_number}`);
            }
        });
        populate_panel_list(page, true);
    }

    else if (page.id === 'panel') {
        page.querySelector('#map').addEventListener('click', function() {
            console.log(page.data);
            document.querySelector('#myNavigator').pushPage('map-overlay.html', {data: page.data});
        });
        console.log(page.data);
        display_panel(page);
    }

    else if (page.id === 'map-overlay') {
        display_map(page);
    }

    else if (page.id === 'config') {
        page.querySelector('#submit').addEventListener('click', function() {
            document.querySelector('#myNavigator').popPage();
        });
        page.querySelector('#cancel').addEventListener('click', function() {
            document.querySelector('#myNavigator').popPage();
        });
    }

});

document.addEventListener('show', function(event) {
    var page = event.target;

    console.log(`Running show for ${page.id}`);

});

document.addEventListener('hide', function(event) {
    var page = event.target;

    console.log(`Running hide for ${page.id}`);

});

document.addEventListener('destroy', function(event) {
    var page = event.target;

    console.log(`Running destroy for ${page.id}`);

});

function display_panel(page) {
    console.log(page);
    let panel_config = PANELS[page.data.panel_number];
    console.log(panel_config);
    let widget_type = panel_config.widget;

    let widget_container = page.querySelector('#widget-container');
    clear_element(widget_container);

    let container_el = document.createElement('div');
    container_el.id = 'widget-' + widget_type;
    container_el.classList.add('widget', widget_type);
    widget_container.appendChild(container_el);

    let widget = null;
    switch (widget_type) {
    case 'weather':
        widget = new Weather('0');
        page.querySelector('#map').hidden = true;
        break;
    case 'station_board':
        widget = new StationBoard('0');
        page.querySelector('#map').hiddden = true;
        break;
    case 'stop_timetable':
        widget = new StopTimetable('0');
        page.querySelector('#map').hidden = false;
        RTMONITOR_API = new RTMonitorAPI();
        break;
    }

    widget.display(
        {
            container_id: 'widget-' + widget_type,
            static_url: `/static_web/smartpanel/widgets/${panel_config.widget}/`,
            display_id: '', layout_id: '',
            rt_token: '778',
            layout_name: 'Layouts for mobile',
            display_name: '', layout_owner: '',
            display_owner: '',
            settings: WIDGET_CONFIG
        },
        panel_config.data
    );

    if (widget_type === 'stop_timetable') {
        RTMONITOR_API.init();
    }

}

function display_map(page) {
    console.log('Dispay map', page);
    let panel_config = PANELS[page.data.panel_number];
    console.log(panel_config);

    // Synthesise a stop_bus_map widget config
    let map_config = {
        'title': panel_config.data.title,
        'map': {
            'zoom': 13,
            'lat': panel_config.data.stop.latitude,
            'lng': panel_config.data.stop.longitude,
        },
        'breadcrumbs': true,
        'stops': [
            panel_config.data.stop
        ]
    };

    let overlay_container = page.querySelector('#overlay-container');
    clear_element(overlay_container);

    let container_el = document.createElement('div');
    container_el.id = 'widget-stop_bus_map';
    container_el.classList.add('widget', 'stop_bus_map', 'full-screen');
    overlay_container.appendChild(container_el);

    let map_widget = new StopBusMap(0);
    map_widget.display(
        {
            container_id: 'widget-stop_bus_map',
            static_url: `/static_web/smartpanel/widgets/stop_bus_map/`,
            display_id: '', layout_id: '',
            rt_token: '778',
            layout_name: 'Layouts for mobile',
            display_name: '', layout_owner: '',
            display_owner: '',
            settings: WIDGET_CONFIG
        },
        map_config
    );
}

// Update the list on the 'pannels' page with the current panels
function populate_panel_list(page, edit) {
    let list = page.querySelector('.panel-items');

    // Remove existing entries
    clear_element(list);

    // Populate
    for (let panel_number = 0; panel_number < PANELS.length; panel_number++) {
        let panel_config = PANELS[panel_number];
        let item = document.createElement('ons-list-item');
        item.innerHTML = `<div class="center">[ICON] ${panel_config.title}</div>`;

        if (edit) {
            item.setAttribute('modifier', 'longdivider');
            let buttons = document.createElement('div');
            buttons.classList.add('right');
            buttons.innerHTML =
                '<ons-icon class="item-edit" icon="ion-edit"></ons-icon>&nbsp;' +
                '<ons-icon class="item-delete" icon="ion-ios-trash, material:ion-andriod-trash"></ons-icon>';
            item.appendChild(buttons);
        }
        else {
            item.setAttribute('modifier', 'chevron longdivider');
            item.setAttribute('tappable', '');
        }

        /*
        let edit = document.createElement('span');
        edit.classList.add('edit');
        edit.addEventListener('click', function() {
            display_config(panel_number);
        });
        edit.innerHTML = '[edit]';

        let del = document.createElement('span');
        del.classList.add('del');
        del.addEventListener('click', function() {
            PANELS.splice(panel_number, 1);
            STORAGE.setItem('MOBILE_PANELS', JSON.stringify(PANELS));
            populate_panel_list();
        });
        del.innerHTML = '[delete]';
        */
        list.appendChild(item);
    }

}

// Find the position of a node within its containing element
function getElementIndex(node) {
    var index = 0;
    while ( (node = node.previousElementSibling) ) {
        index++;
    }
    return index;
}

// Remove all the child elements of el
function clear_element(el) {
    while (el.firstChild) {
        el.removeChild(el.firstChild);
    }
}
