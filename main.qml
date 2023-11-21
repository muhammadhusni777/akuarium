import QtQuick 2.12
import QtQuick.Window 2.13
import QtQuick.Controls 2.0
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0

import QtQuick 2.15
import QtQuick.Controls 2.15

Window {
    visible: true
    width: 400
    height: 400
    title: "Aquarium Husni"
	color : "#9cd3db"
    property var xValues: [] // contoh nilai x
    property var yValues: [] // contoh nilai y
	property var mirror_x: []

    Rectangle {
        anchors.fill: parent
		color : "transparent"

        Repeater {
            model: Math.min(xValues.length, yValues.length, mirror_x.length)

           
				
				
				
				Image{
				x: xValues[index]
                y: yValues[index]
				width : 100
				height : 70
				source:"marlin.png"
				mirror: JSON.parse(mirror_x[index])
				
            }
        }
    }
	
	
	Button{
	x: 300
	y: 300
	text : "tambah ikan"
	
	
	onClicked:{
	backend.tambah_ikan("yes")
	}
	}
	
	
	Button{
	x: 300
	y: 350
	text : "kurang ikan"
	
	
	onClicked:{
	backend.kurang_ikan("yes")
	}
	}
	
	Timer{
		id: gui_timer
		interval: 100
		repeat: true
		running: true
		onTriggered: {
		xValues = backend.array_x()
		yValues = backend.array_y()
		mirror_x = backend.mirror()
		//console.log(mirror_x[index])
		backend.shuffle("yes")
		
		}
		
		}
		
		
	Timer{
		id: head
		interval: 3000
		repeat: true
		running: true
		onTriggered: {
			backend.mirror_orientation("yes")
		
		}
		}
}













