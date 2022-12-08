library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

ENTITY demux24 IS port(
  g, c, b, a: IN std_logic;
  y: OUT std_logic_vector(0 to 3));
END demux24;

ARCHITECTURE arch OF demux24 IS 
	signal en: std_logic;

BEGIN
	en <= not g;
	y(0) <= not (en and not b and not a and c);
	y(1) <= not (en and not b and a and c);
	y(2) <= not (en and b and not a and c);
	y(3) <= not (en and b and a and c);

END arch;

