-- AI agent 'Rushing Charge':
DELETE FROM `ai_agents` WHERE `spell` = 6268 AND `entry` 
IN ( 3122, 3123, 3227 );

-- AI agent 'Boar Charge':
DELETE FROM `ai_agents` WHERE `spell` = 3385 AND `entry` 
IN ( 3099, 3100, 3225 );