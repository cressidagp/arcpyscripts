'''

Engine: APE
Zone: Global
Creature: Zeppelin Masters

'''

import arcemu
from arcemu import GameObject
from arcemu import Unit

'''
#gameObjectId, route, mapid( mapIdOrzoneIdOrAreaId ), npcId, message
OBJECT_DATA = [
    [ 285, 175080, 0, 3149, "The zeppelin to Orgrimmar has just arrived! All aboard for Durotar!" ],
    [ 285, 175080, 1, 12136, "The zeppelin to Grom'gol has just arrived! All aboard for Stranglethorn!" ],
    [ 301, 176495, 0, 12137, "The zeppelin to Undercity has just arrived! All aboard for Tirisfal Glades!" ],
    [ 301, 176495, 0, 3150, "The zeppelin to Grom'gol has just arrived! All aboard for Stranglethorn!" ],
    [ 302, 164871, 0, 9566, "The zeppelin to Orgrimmar has just arrived! All aboard for Durotar!" ],
    [ 302, 164871, 1, 9564, "The zeppelin to Undercity has just arrived! All aboard to Tirisfall Glades!" ],
 
    [ 712, 186238, 9, 26537, "The zeppelin to Warsong Hold has just arrived! All aboard for Borean Tundra!" ],
    [ 712, 186238, 9, 26538, "The zeppelin to Orgrimmar has just arrived! All aboard for Durotar!" ],

    [ 737, 195459, 9, 26539, "The zeppelin to Vengeance Landing has just arrived! All aboard for Howling Fjord!" ],
    [ 737, 195459, 9, 26540, "The zeppelin to Undercity has just arrived! All aboard for Tirisfal Glades!" ],

    [ 1221, 190549, 9, 34765, "The zeppelin to Thunder Bluff has arrived! All aboard for a smooth ride across the Barrens!" ],
    [ 1221, 190549, 9, 34766, "Step right up! The zeppelin to Orgrimmar has arrived! All aboard to Durotar!" ]
]
#create list
ZEPPELIN_MASTERS_NPC_ID = [ 3149, 3150, 9564, 9566, 12136, 12137, 26537, 26538, 26539, 26540, 34765, 34766 ]
'''

ZEPPELIN_MASTERS_TEXT = [
"The zeppelin to Orgrimmar has just arrived! All aboard for Durotar!",
"The zeppelin to Grom'gol has just arrived! All aboard for Stranglethorn!",
"The zeppelin to Undercity has just arrived! All aboard for Tirisfal Glades!",
"The zeppelin to Vengeance Landing has just arrived! All aboard for Howling Fjord!",
"The zeppelin to Warsong Hold has just arrived! All aboard for Borean Tundra!",
"The zeppelin to Thunder Bluff has arrived! All aboard for a smooth ride across the Barrens!"
]

def zeppelin_onTransportArrive( go, route ):
    mapMgr = go.getMapMgr()

    # Stranglethorn <=> Durotar
    if route == 285:
        mapId = go.getMapId()
        if mapId == 0:
            zm = mapMgr.getCreatureNearestCoords( -12441.30, 215.02, 31.32, 3149 )
            if zm:
              zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 0 ] )  

        else:
           zm = mapMgr.getCreatureNearestCoords( 1354.03, -4642.61, 53.63, 12136 )
           if zm:
               zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 1 ] )

    # Tirisfall Glades <=> Stranglethorn
    if route == 301:
        zoneId = go.getZoneId()
        if zoneId == 0:
            zm = mapMgr.getCreatureNearestCoords( 2054.57, 241.68, 99.85, 3150 )
            if zm:
                zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 1 ] )
        
        else:
            zm = mapMgr.getCreatureNearestCoords( 2366.48, -2548.22, 103.27, 12737 )
            if zm:
                zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 2 ] )

    # Tirisfall Glades <=> Durotar
    if route == 302:
        mapId = go.getMapId()
        if mapId == 0:
            zm = mapMgr.getCreatureNearestCoords( 2064.01, 288.57, 97.11, 9566 )
            if zm:
                zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 0 ] )

        else:
            zm = mapMgr.getCreatureNearestCoords( 1331.10, -4649.45, 53.03, 9564 )
            if zm:
               zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 2 ] )

    # Durotar <=> Borean Tundra
    if route == 712:
        mapId = go.getMapId()
        if mapId == 1:
            zm = mapMgr.getCreatureNearestCoords( 1174.52, -4152.51, 51.73, 26537 )
            if zm:
                zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 4 ] )
        else:
            zm = mapMgr.getCreatureNearestCoords( 2817.72, 6177.08, 122.21, 26538 )
            if zm:
                zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 0 ] )

    # Tirisfall Glades <=> Howling Fjord
    if route == 737:
        mapId = go.getMapId()
        if mapId == 0:
            zm = mapMgr.getCreatureNearestCoords( 2058.06, 357.59, 82.55, 26539 )
            if zm:
                zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 3 ] )
        
        else:
            zm = mapMgr.getCreatureNearestCoords( 1975.03, -6095.22, 67.22, 26540 )
            if zm:
                zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 2 ] )

    # Durotar <=> Mulgore
    if route == 1221:
        zoneId = go.getZoneId()
        if zoneId == 0:
            zm = mapMgr.getCreatureNearestCoords( 1149.00, -4152.21, 51.73, 34765 )
            if zm:
                zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 5 ] )
        
        else:
            zm = mapMgr.getCreatureNearestCoords( -1032.50, 313.14, 135.00, 34766 )
            if zm:
                zm.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, ZEPPELIN_MASTERS_TEXT[ 0 ] )

arcemu.RegisterServerHook( arcemu.SERVER_HOOK_EVENT_ON_TRANSPORT_ARRIVED, zeppelin_onTransportArrive )