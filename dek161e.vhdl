library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- warning: this file will not be saved if:
--     * following entity block contains any syntactic errors (e.g. port list isn't separated with ; character)
--     * following entity name and current file name differ (e.g. if file is named mux41 then entity must also be named mux41 and vice versa)
ENTITY dek416e IS port(
	e: in std_logic;
	a: in std_logic_vector(0 to 3);
	y: out std_logic_vector(0 to 15));
END dek416e;

ARCHITECTURE arch OF dek416e IS 
	signal prva_raz: std_logic_vector(0 to 1);
	signal druga_raz: std_logic_vector(0 to 3);
	signal treca_raz: std_logic_vector(0 to 7);

BEGIN
	
	dk11: entity work.dek12e port map (e => e, a => a(0), y0 => prva_raz(0), y1 => prva_raz(1));
	
	dk21: entity work.dek12e port map (e => prva_raz(0), a => a(1), y0 => druga_raz(0), y1 => druga_raz(1));
	dk22: entity work.dek12e port map (e => prva_raz(1), a => a(1), y0 => druga_raz(2), y1 => druga_raz(3));

	dk31: entity work.dek12e port map (e => druga_raz(0), a => a(2), y0 => treca_raz(0), y1 => treca_raz(1));
	dk32: entity work.dek12e port map (e => druga_raz(1), a => a(2), y0 => treca_raz(2), y1 => treca_raz(3));
	dk33: entity work.dek12e port map (e => druga_raz(2), a => a(2), y0 => treca_raz(4), y1 => treca_raz(5));
	dk34: entity work.dek12e port map (e => druga_raz(3), a => a(2), y0 => treca_raz(6), y1 => treca_raz(7));
	
	dk41: entity work.dek12e port map (e => treca_raz(0), a => a(3), y0 => y(0), y1 => y(1));
	dk42: entity work.dek12e port map (e => treca_raz(1), a => a(3), y0 => y(2), y1 => y(3));
	dk43: entity work.dek12e port map (e => treca_raz(2), a => a(3), y0 => y(4), y1 => y(5));
	dk44: entity work.dek12e port map (e => treca_raz(3), a => a(3), y0 => y(6), y1 => y(7));
	dk45: entity work.dek12e port map (e => treca_raz(4), a => a(3), y0 => y(8), y1 => y(9));
	dk46: entity work.dek12e port map (e => treca_raz(5), a => a(3), y0 => y(10), y1 => y(11));
	dk47: entity work.dek12e port map (e => treca_raz(6), a => a(3), y0 => y(12), y1 => y(13));
	dk48: entity work.dek12e port map (e => treca_raz(7), a => a(3), y0 => y(14), y1 => y(15));
	

END arch;