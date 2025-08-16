-- Sputtervalve
DELETE FROM npc_gossip_textid WHERE creatureid = 3442;

-- Fandral Staghelm
DELETE FROM npc_gossip_textid WHERE creatureid = 3516;

-- Jenal
DELETE FROM npc_gossip_textid WHERE creatureid = 9047;

-- Knight Defender Zunade
DELETE FROM npc_gossip_textid WHERE creatureid = 18030;

-- Thomas Miller
DELETE FROM npc_monstersay WHERE entry = 3518 and event = 1;

-- ICC: The Damned
DELETE FROM ai_agents WHERE entry = 37011;