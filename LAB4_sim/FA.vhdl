library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- warning: this file will not be saved if:
--     * following entity block contains any syntactic errors (e.g. port list isn't separated with ; character)
--     * following entity name and current file name differ (e.g. if file is named mux41 then entity must also be named mux41 and vice versa)
ENTITY FA IS port(
	a, b: in std_logic_vector(1 downto 0);
	r: out std_logic_vector(1 downto 0);
	cin: in std_logic;
	cout: out std_logic);	

END FA;

ARCHITECTURE arch OF FA IS 

BEGIN
	
	r(1) <= (not cin and ( (not a(1) and not a(0) and     b(0)) or 
	                       (not a(1) and     a(0) and not b(1)) or 
	                       (    a(1) and     a(0) and not b(0)) or
	                       (    a(1) and not a(0) and     b(1)) ) )
	       or
	       (cin and ( (not a(1) and not a(0) and     b(1)) or
	                  (not a(1) and     a(0) and     b(0)) or
	                  (    a(1) and     a(0) and not b(1)) or
	                  (    a(1) and not a(0) and not b(0)) ) );
	                  
	r(0) <= (not cin and ( (not a(1) and not a(0) and not b(1)) or 
	                       (not a(1) and	 a(0) and not b(0)) or 
	                       (	a(1) and	 a(0) and	 b(1)) or
	                       (	a(1) and not a(0) and	 b(0)) ) )
	       or
	       (cin and ( (not a(1) and not a(0) and     b(0)) or
	                  (not a(1) and     a(0) and not b(1)) or
	                  (	   a(1) and     a(0) and not b(0)) or
	                  (    a(1) and not a(0) and     b(1)) ) );
	                
	cout <= (not a(1) and not b(1)) or
			(not a(1) and not a(0) and b(0)) or
			(a(0) and not b(1) and not b(0)) or
			(cin and ((not b(1) and not b(0)) or
			          (not a(1) and not a(0)) or
			          (not a(1) and b(0)) or
			          (a(0) and not b(1))) );

END arch;