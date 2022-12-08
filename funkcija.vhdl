library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- warning: this file will not be saved if:
--     * following entity block contains any syntactic errors (e.g. port list isn't separated with ; character)
--     * following entity name and current file name differ (e.g. if file is named mux41 then entity must also be named mux41 and vice versa)
ENTITY funkcija IS port(
	a, b, c, d: in std_logic;
	f: out std_logic);
END funkcija;

ARCHITECTURE arch OF funkcija IS 
	signal dek: std_logic_vector(0 to 15);
BEGIN
	oznaka: entity work.dek416e port map (e => '1', a(0) => a, a(1) => b, a(2) => c, a(3) => d, y => dek);
	f <= dek(X) or dek(X) or dek(X) or dek(X) or ... ;
	--zamijenite X s mintermima vase funkcije

END arch;