import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

Window {
    id: root

    width: 640
    height: 480
    visible: true
    Item{
        id : page
        visible:true
        width: parent.width

        Rectangle {
            id : 'myrectangle'
            width: parent.width
            height:{
                console.log('I am a comment')
                return 160
            }
            color: '#f00'
            Text {
                id:'mainText'
                text : 'Kesi is learning'
                height: 50
                width:parent.width
                font.pixelSize:12
                horizontalAlignment: Text.AlignHCenter

            }
            Button{
                id:mainbutton
                text:'Click'
                anchors.top: mainText.bottom
                onClicked:{
                    console.log(myrectangle.color)
                    if(myrectangle.color == '#fff'){
                        myrectangle.color = '#f00'
                    }else{
                        myrectangle.color = '#fff'
                    }

                }
            }
        }
    }

}