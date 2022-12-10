library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- warning: this file will not be saved if:
--     * following entity block contains any syntactic errors (e.g. port list isn't separated with ; character)
--     * following entity name and current file name differ (e.g. if file is named mux41 then entity must also be named mux41 and vice versa)
ENTITY zbrajalo IS port(
	a, b: in std_logic_vector(7 downto 0);
	oper: in std_logic;
	r: out std_logic_vector(7 downto 0));

END zbrajalo;

ARCHITECTURE arch OF zbrajalo IS 
	signal c: std_logic_vector(3 downto 0);
BEGIN

	fa1: entity work.primitiv port map (a => a(1 downto 0), b => b(1 downto 0), oper => oper, cin => oper, cout => c(0), r => r(1 downto 0));
	fa2: entity work.primitiv port map (a => a(3 downto 2), b => b(3 downto 2), oper => oper, cin => c(0), cout => c(1), r => r(3 downto 2));
	fa3: entity work.primitiv port map (a => a(5 downto 4), b => b(5 downto 4), oper => oper, cin => c(1), cout => c(2), r => r(5 downto 4));
	fa4: entity work.primitiv port map (a => a(7 downto 6), b => b(7 downto 6), oper => oper, cin => c(2), cout => c(3), r => r(7 downto 6));	

END arch;