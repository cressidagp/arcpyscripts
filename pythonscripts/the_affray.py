'''
.npc portto 43359
.quest start 1718 (the islander)

TODO:

*) setOrientation of challengers when spawn
*) check player class since its a warrior quest
*) check objective completion
*) add plr name on text

'''
import arcemu
import ArcPyMath as Math
from arcemu import Unit
from arcemu import Player

#THE_AFFRAY = {}

THE_AFFRAY_TEXTS = [
"The Affray has begun.  $n, get ready to fight!",
"You!  Enter the fray!",
"Challenger is down!",
"The Affray is over!"
]

theAffrayCoords = [
[ -1683.0, -4326.0, 2.79, 0 ],
[ -1682.0, -4329.0, 2.79, 0 ],
[ -1683.0, -4330.0, 2.79, 0 ],
[ -1680.0, -4334.0, 2.79, 1.49 ],
[ -1674.0, -4326.0, 2.79, 3.49 ],
[ -1677.0, -4334.0, 2.79, 1.66 ]
]

theAffrayDisplays = [ 4968, 4969, 4970, 4971 ]

QUESTID_THE_AFFRAY = 1719
CREATUREID_TWIGGY_FLATHEAD = 6248
CREATUREID_AFFRAY_CHALLENGER = 6240
CREATUREID_BIG_WILL = 6238

theAffaryVars = {
    "eventInProgress": False,
    "eventGrate": False,
    "affrayChallenger":[ None, None, None, None, None, None ],
    "challengerDown":[ False, False, False, False, False, False ],
    "waveTimer": 0,
    "challengerChecker": 0,
    "eventBigWill": False,
    "wave": 1,
    "bigWill" : 0,
    "plr_Guid": None
}

def twiggyFlathead_onAIUpdate( unit, event ):

    creature = unit.toCreature()
    objects = creature.getObjectsInRange()

    for o in objects:
        u = arcemu.toUnit( o )
        if u is not None and theAffaryVars["eventInProgress"] == False:
            if u.isPlayer(): #and plr class its warrior and GetQuestObjectiveCompletion(1719, 0) == 0
                if unit.calcDistance( u ) <= 20:
                    theAffaryVars["eventInProgress"] = True
                    theAffaryVars["plr_Guid"] = u.getGUID()
                    #print(theAffaryVars["plr_Guid"])
                    #print(theAffaryVars["eventInProgress"])

    if theAffaryVars["eventGrate"] == False and theAffaryVars["eventInProgress"] == True:

        mapMgr = creature.getMapMgr()
        p = mapMgr.getUnit(theAffaryVars["plr_Guid"])
        plr = p.toPlayer()
        if plr.hasQuest( QUESTID_THE_AFFRAY ):
            x = plr.getPositionX()
            y = plr.getPositionY()
            #maybe we should use that AT in the center of the circle...
            if( x >= -1684 and x <= -1674 and y >= -4334 and y <= -4324 ):
                unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, THE_AFFRAY_TEXTS[ 0 ] )
                for i in range ( 6 ):
                    mob = mapMgr.spawnCreature( CREATUREID_AFFRAY_CHALLENGER, theAffrayCoords[ i ][ 0 ], theAffrayCoords[ i ][ 1 ], theAffrayCoords[ i ][ 2 ] )
                    #mob.SetOrientation( theAffrayCoords[ i ][ 3 ])
                    mob.setDisplayId( theAffrayDisplays[Math.randomUInt( 3 )] )
                
                theAffaryVars["eventGrate"] = True
                theAffaryVars["waveTimer"] = 5
                theAffaryVars["affrayChallenger"] = 1

    if theAffaryVars["eventInProgress"] == True:

        diff = theAffaryVars["waveTimer"]
        diff = diff - 1
        theAffaryVars["waveTimer"] = diff

        if theAffaryVars["challengerChecker"] <= 1:
            for i in range ( 6 ):
                if theAffaryVars["affrayChallenger"][ i ]:
                    npc = unit.GetUnit( theAffaryVars["affrayChallenger"][ i ] )
                    

                  

def twiggyFlathead_onLoad( unit, event ):
    unit.RegisterAIUpdateEvent( 1000 )

arcemu.RegisterUnitEvent( CREATUREID_TWIGGY_FLATHEAD, arcemu.CREATURE_EVENT_ON_LOAD, twiggyFlathead_onLoad )
arcemu.RegisterUnitEvent( CREATUREID_TWIGGY_FLATHEAD, arcemu.CREATURE_EVENT_ON_AIUPDATE, twiggyFlathead_onAIUpdate )