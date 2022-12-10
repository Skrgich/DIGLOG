library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- warning: this file will not be saved if:
--     * following entity block contains any syntactic errors (e.g. port list isn't separated with ; character)
--     * following entity name and current file name differ (e.g. if file is named mux41 then entity must also be named mux41 and vice versa)
ENTITY b1kompl IS port(
	x: in std_logic_vector(1 downto 0);
	y: out std_logic_vector(1 downto 0));
	
END b1kompl;

ARCHITECTURE arch OF b1kompl IS 

BEGIN
	y(1) <= not x(1) after 10 ns;
	y(0) <= x(0) after 10 ns;	

END arch;