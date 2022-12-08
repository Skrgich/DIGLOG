library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- warning: this file will not be saved if:
--     * following entity block contains any syntactic errors (e.g. port list isn't separated with ; character)
--     * following entity name and current file name differ (e.g. if file is named mux41 then entity must also be named mux41 and vice versa)
ENTITY dek12e IS port(
	e, a: IN std_logic;
	y0, y1: OUT std_logic);
	
END dek12e;

ARCHITECTURE arch OF dek12e IS 

BEGIN

	y0 <= e and not a after 10 ns;
	y1 <= e and a after 10 ns;

END arch;