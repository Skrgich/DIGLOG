library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

ENTITY demux38 IS port(
	g, c, b, a: IN std_logic;
	y: OUT std_logic_vector(0 to 7));
END demux38;

ARCHITECTURE arch OF demux38 IS 
	signal cc: std_logic;

BEGIN
	cc <= not c;
	dm1: entity work.demux24 port map (g => g, c => cc, b => b, a => a, y => y(0 to 3));
	dm2: entity work.demux24 port map (g => g, c => c, b => b, a => a, y => y(4 to 7));
END arch;