import arcemu

#SPELLID_PLAY_MOVIE = 73159

def playMovie_handleScriptedEffect( effectIndex, spell ):
    caster = spell.getCaster()
    c = arcemu.toCreature( caster )

    if c is not None:
        objects = c.getObjectsInRange()
        for o in objects:
            u = arcemu.toUnit( o )
            if u is not None:
                if u.isPlayer():
                    p = u.toPlayer()
                    p.sendMovie( 16 )
    return True

arcemu.RegisterScriptedEffectHandler( 73159, playMovie_handleScriptedEffect )