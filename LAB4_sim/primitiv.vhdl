library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- warning: this file will not be saved if:
--     * following entity block contains any syntactic errors (e.g. port list isn't separated with ; character)
--     * following entity name and current file name differ (e.g. if file is named mux41 then entity must also be named mux41 and vice versa)
ENTITY primitiv IS port(
	a, b: in std_logic_vector(1 downto 0);
	oper, cin: in std_logic;
	cout: out std_logic;
	r: out std_logic_vector(1 downto 0));
	
END primitiv;

ARCHITECTURE arch OF primitiv IS 
	signal b_komp, z: std_logic_vector(1 downto 0);

BEGIN
	bk: entity work.b1kompl port map (x => b, y => b_komp);
	dm: entity work.dmux port map (x => b, y => b_komp, z => z, s => oper);
	zb: entity work.FA port map (a => a, b => z, r => r, cin => cin, cout => cout);

END arch;