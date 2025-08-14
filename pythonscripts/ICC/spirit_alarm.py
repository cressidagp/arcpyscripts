import arcemu
import ArcPyMath as Math
from arcemu import Unit
from arcemu import ObjectLocator
from arcemu import GameObjectScript

SPELLID_SPIRIT_ALARM_1 = 70536
SPELLID_SPIRIT_ALARM_2 = 70545
SPELLID_SPIRIT_ALARM_3 = 70546
SPELLID_SPIRIT_ALARM_4 = 70547

SPELLID_STONEFORM = 70733

#EVENT_AWAKEN_WARD_1 = 22900
#EVENT_AWAKEN_WARD_2 = 22907
#EVENT_AWAKEN_WARD_3 = 22908
#EVENT_AWAKEN_WARD_4 = 22909

#GO_SPIRIT_ALARM_1 = 201814
#GO_SPIRIT_ALARM_2 = 201815
#GO_SPIRIT_ALARM_3 = 201816
#GO_SPIRIT_ALARM_4 = 201817

NPC_DEATHBOUND_WARD = 37007

WARD_TEXTS = [
"The master's sanctum has been disturbed!",
"I... awaken!",
"Who... goes there...?"
]

WARD_SOUNDS = [ 16865, 16866, 16867 ]

class spirit_alarm_Script( GameObjectScript ):
    def __init__( self, go ):
        GameObjectScript.__init__( self, go )

    def OnSpawn( self ):
        go = self.gameobject
        #go.setByteFlags( 0x0006+0x000B, 1, 22 )
        go.RegisterAIUpdateEvent( 3000 )
    
    def AIUpdate( self ):
        go = self.gameobject
        locator = ObjectLocator( go )
        p = locator.findClosestPlayer()
        print(p)
        #u = arcemu.toUnit( go )
        #p.castSpell( SPELLID_SPIRIT_ALARM_1, True, p )

    @staticmethod
    def create( go ):
        return spirit_alarm_Script( go )


def spirit_alarm_handleScriptedEffect( effectIndex, spell ):
    trapId = 0

    if effectIndex == 22900:
        trapId = 201814
    elif effectIndex == 22907:
        trapId = 201815
    elif effectIndex == 22908:
        trapId = 201816
    elif effectIndex == 22909:
        trapId = 201817
    
    trap = spell.getCaster()

    objects = trap.getObjectsInRange()

    for o in objects:
        u = arcemu.toUnit( o )
        if u is not None:
            c = arcemu.toCreature( u )
            if c is not None:
                if c.getId() == NPC_DEATHBOUND_WARD and u.hasAura( SPELLID_STONEFORM ):
                    a = u.getAuraBySpellId( SPELLID_STONEFORM )
                    if a is not None:
                        a.remove()
                        random = Math.randomUInt( 2 )
                        c.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, WARD_TEXTS[ random ] )
                        c.playSoundToSet( WARD_SOUNDS[ random ] )
                        break


arcemu.RegisterGameObjectScript( 201814, spirit_alarm_Script.create )
arcemu.RegisterGameObjectScript( 201815, spirit_alarm_Script.create )
arcemu.RegisterGameObjectScript( 201816, spirit_alarm_Script.create )
arcemu.RegisterGameObjectScript( 201817, spirit_alarm_Script.create )
arcemu.RegisterScriptedEffectHandler( SPELLID_SPIRIT_ALARM_1, spirit_alarm_handleScriptedEffect )
arcemu.RegisterScriptedEffectHandler( SPELLID_SPIRIT_ALARM_2, spirit_alarm_handleScriptedEffect )
arcemu.RegisterScriptedEffectHandler( SPELLID_SPIRIT_ALARM_3, spirit_alarm_handleScriptedEffect )
arcemu.RegisterScriptedEffectHandler( SPELLID_SPIRIT_ALARM_4, spirit_alarm_handleScriptedEffect )