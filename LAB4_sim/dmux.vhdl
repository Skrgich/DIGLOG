library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- warning: this file will not be saved if:
--     * following entity block contains any syntactic errors (e.g. port list isn't separated with ; character)
--     * following entity name and current file name differ (e.g. if file is named mux41 then entity must also be named mux41 and vice versa)
ENTITY dmux IS port(
	x, y: in std_logic_vector(1 downto 0);
	s: in std_logic;	
	z: out std_logic_vector(1 downto 0));
	
END dmux;

ARCHITECTURE arch OF dmux IS 

BEGIN

	z(1) <= (not s and x(1)) or (s and y(1)) after 10 ns;
	z(0) <= (not s and x(0)) or (s and y(0)) after 10 ns;

END arch;