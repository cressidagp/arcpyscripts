import arcemu
import ArcPyMath as Math
from arcemu import Unit

NETHERSTORM_AGENT_TEXTS = [
"Good thing that we're surrounded by neighbors with excess machine parts.",
"Maybe I should gather up some other agents and head out there after this shift?",
"Hmm, arcane annihilators are pretty tough.  I wonder if Papa Wheeler knows what he's asking for?",
"Last time someone went out to try to collect the bounty on Netherock, all we got back was a compressed layer of foolhardy adventurer!",
"Netherock?!  That thing'll squish you flat with one step of its massive foot!  No thanks!"
]

NPCID_NETHERSTORM_AGENT = 19541

def NetherstormAgent_onLoad( unit, event ):

    unit.RegisterAIUpdateEvent( 60000 )

def NetherstormAgent_onAIUpdate( unit, event ):

    chance = Math.randomUInt( 2 )

    if chance == 1:
     
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, NETHERSTORM_AGENT_TEXTS[ Math.randomUInt( 4 ) ] )

arcemu.RegisterUnitEvent( NPCID_NETHERSTORM_AGENT, arcemu.CREATURE_EVENT_ON_LOAD, NetherstormAgent_onLoad )
arcemu.RegisterUnitEvent( NPCID_NETHERSTORM_AGENT, arcemu.CREATURE_EVENT_ON_AIUPDATE, NetherstormAgent_onAIUpdate )