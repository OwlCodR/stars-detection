https://cdsarc.cds.unistra.fr/viz-bin/cat/B/vsx#/browse

B/vsx       AAVSO International Variable Star Index VSX     (Watson+, 2006-2014)
================================================================================
The AAVSO International Variable Star Index (Version 2022-04-19)
    Watson C., Henden A.A., Price A.
   <AAVSO (2009)>
   =2006SASS...25...47W
   =2015yCat....102027W
================================================================================
ADC_Keywords: Stars, variable ;

Description:
    This file contains Galactic stars known or suspected to be variable.
    It lists all stars that have an entry in the AAVSO International
    Variable Star Index (VSX; http://www.aavso.org/vsx).

    The database consisted initially of the General Catalogue of Variable
    Stars (GCVS) and the New Catalogue of Suspected Variables (NSV) and
    was then supplemented with a large number of variable star catalogues,
    as well as individual variable star discoveries or variables found in
    the literature. Effort has also been invested to update the entries
    with the latest information regarding position, type and period and to
    remove duplicates. The VSX database is being continually updated and
    maintained.

    For historical reasons some objects outside of the Galaxy have been
    included.

See also:
   B/gcvs : General Catalogue of Variable Stars (Samus+ 2007-2009)
   http://www.aavso.org/ : the American Associatation of Variable Star Observers


File Summary:
--------------------------------------------------------------------------------
 FileName   Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe         80        .   This file
vsx.dat       158   2117467  Variable Star indeX, Version 2022-04-19
refs.dat       27   830415   Bibliography (references) of VSX stars
vsx_id.dat     58        1   Stars having a "VSX" name
--------------------------------------------------------------------------------

Byte-by-byte Description of file: vsx.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label    Explanations
--------------------------------------------------------------------------------
   1-  7  I7    ---     OID      Internal identifier, can be used to
                                 link out to the VSX database (1)
   9- 38  A30   ---     Name     Variable star identifier
      40  I1    ---     V        [0,3] Variability flag (2)
  42- 50  F9.5  deg     RAdeg    Right ascension (J2000)
  52- 60  F9.5  deg     DEdeg    Declination (J2000)
  62- 91  A30   ---     Type     Variability type, as in GCVS catalog
      94  A1    ---   l_max      Limit flag on max
  95-100  F6.3  mag     max      ? Magnitude at maximum, or amplitude
     101  A1    ---   u_max      Uncertainty flag on max
 102-107  A6    ---   n_max      Passband on max magnitude (4)
     109  A1    ---   f_min      [(] '(' indicates an amplitude
     110  A1    ---   l_min      Limit flag on min
 111-116  F6.3  mag     min      ? Magnitude at minimum, or amplitude
     117  A1    ---   u_min      Uncertainty flag on min
 118-123  A6    ---   n_min      Passband on min magnitude (4)
 125-136  F12.4 d       Epoch    ? Epoch of maximum or minimum (HJD)
     137  A1    ---   u_Epoch    [:)] Uncertainty flag (:) on epoch
     139  A1    ---   l_Period   [<>(] Limit flag on period (3)
 140-155 F16.10 d       Period   ? Period of the variable in days
 156-158  A3    ---   u_Period   [:)*/N2 ] Uncertainty flag on Period (3)
--------------------------------------------------------------------------------
Note (1): To get the VSX URL, add the OID to
     http://www.aavso.org/vsx/index.php?view=detail.top&oid=

Note (2): 0 = Variable,
          1 = Suspected variable,
          2 = Constant or non-existing,
          3 = Possible duplicate

Note (3): The value of the period may be preceded by ">" or "<" if the
     period is a lower or upper limit, respectively, or by a "(" which
     indicates that the period is the mean cycle time of a U Gem or
     recurrent nova (a closing bracket exists in u_Period).

     The value of the period may be followed by the following symbols:
     : = uncertainty flag
     ) = value of the mean cycle for U Gem or recurrent nova
         (the corresponding opening bracket exists in l_Period)
     *N = the real period is likely a multiple of the quoted period
     /N = the period quoted is likely a multiple of the real period

Note (4): Passbands include the following:
     U B V R I   = Johnson broad-band
     J H K L M   = Johnson infra-red (1.2, 1.6, 2.2, 3.5, 5{mu}m)
     Rc Ic       = Cousins' red and infra-red
     u v b y     = Stroemgren intermediate-band
     u'g'r'i'z'  = Sloan (SDSS)
     pg pv bj rf = photographic blue (pg, bj) visual (pv), red (rf)
     w C CR CV   = white (clear); R or V used for comparison star.
     R1          = ROTSE-I (450-1000nm)
     Hp T        = Hipparcos and Tycho (Cat. I/239)
     NUV         = near-UV (Galex)
     H1A H1B     = STEREO mission filter (essentially 600-800nm)
--------------------------------------------------------------------------------

Byte-by-byte Description of file: refs.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label    Explanations
--------------------------------------------------------------------------------
   1-  7  I7    ---     OID      Internal identifier, as in file "vsx.dat"
   9- 27  A19   ---     Bibcode  Reference of a paper dealing with the object
--------------------------------------------------------------------------------

Byte-by-byte Description of file: vsx_id.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label    Explanations
--------------------------------------------------------------------------------
   1-  3  A3    ---     ---      [VSX]
   5- 20  A16   ---     VSX      VSX name (JHHMMSS.S+DDMMSS)
      21  A1    ---     ---      [=]
  22- 28  I7    ---     OID      Internal identifier, as in file "vsx.dat"
      29  A1    ---     ---      [=]
  30- 58  A29   ---     Name     Variable star identifier, as in file "vsx.dat"
                                 (when this identifier is not a VSX name)
--------------------------------------------------------------------------------

History:
  * 2009-06-19: OID<=230843, 177741 stars. First version for vizier
  * 2009-08-02: OID<=230991, 177611 stars. Addition of file "refs.dat"
  * 2009-09-13:              178200 stars, from http://www.aavso.org/vsx/
  * 2009-09-27: OID<=232835, 178218 stars, from http://www.aavso.org/vsx/
  * 2009-10-18: OID<=233937, 178516 stars, from http://www.aavso.org/vsx/
  * 2009-10-25: OID<=233949, 178521 stars, from http://www.aavso.org/vsx/
  * 2009-11-01:              171935 stars, from http://www.aavso.org/vsx/
  * 2009-11-08: OID<=238565, 178590 stars, from http://www.aavso.org/vsx/
  * 2009-11-15: OID<=238587, 178599 stars, from http://www.aavso.org/vsx/
  * 2009-11-22: OID<=238709, 178657 stars, from http://www.aavso.org/vsx/
  * 2009-11-29: OID<=238725, 178661 stars, from http://www.aavso.org/vsx/
  * 2009-12-06: OID<=238741, 178669 stars, from http://www.aavso.org/vsx/
  * 2009-12-13:              178823 stars, from http://www.aavso.org/vsx/
  * 2010-01-10: OID<=239183, 178869 stars, from http://www.aavso.org/vsx/
  * 2010-01-31: OID<=239469, 178848 stars, from http://www.aavso.org/vsx/
  * 2010-02-21: OID<=239665, 178945 stars, from http://www.aavso.org/vsx/
  * 2010-02-28: OID<=239705, 178945 stars, from http://www.aavso.org/vsx/
  * 2010-03-14: OID<=240107, 178744 stars, from http://www.aavso.org/vsx/
  * 2010-03-21: OID<=241147, 179227 stars, from http://www.aavso.org/vsx/
  * 2010-04-05: OID<=241217, 179221 stars, from http://www.aavso.org/vsx/
  * 2010-04-25: OID<=241439, 179311 stars, from http://www.aavso.org/vsx/
  * 2010-05-02: OID<=241465, 179321 stars, from http://www.aavso.org/vsx/
  * 2010-05-23: OID<=241573, 179367 stars, from http://www.aavso.org/vsx/
  * 2010-05-30: OID<=241843, 179498 stars, from http://www.aavso.org/vsx/
  * 2010-06-06: OID<=241899, 179448 stars, from http://www.aavso.org/vsx/
  * 2010-06-13: OID<=241911, 179449 stars, from http://www.aavso.org/vsx/
  * 2010-06-20:              179479 stars, from http://www.aavso.org/vsx/
  * 2010-06-27: OID<=241981, 181053 stars, from http://www.aavso.org/vsx/
  * 2010-07-04: OID<=245485, 181127 stars, from http://www.aavso.org/vsx/
  * 2010-07-11: OID<=245581, 181163 stars, from http://www.aavso.org/vsx/
  * 2010-07-25: OID<=245665, 181203 stars, from http://www.aavso.org/vsx/
  * 2010-08-01: OID<=245731, 181235 stars, from http://www.aavso.org/vsx/
  * 2010-08-08: OID<=245765, 181252 stars, from http://www.aavso.org/vsx/
  * 2010-08-15: OID<=248445, 182541 stars, from http://www.aavso.org/vsx/
  * 2010-08-22: OID<=249225, 182720 stars, from http://www.aavso.org/vsx/
  * 2010-08-29: OID<=249265, 182654 stars, from http://www.aavso.org/vsx/
  * 2010-09-05: OID<=249331, 182684 stars, from http://www.aavso.org/vsx/
  * 2010-09-12: OID<=249375, 182701 stars, from http://www.aavso.org/vsx/
  * 2010-09-26: OID<=249605, 182771 stars, from http://www.aavso.org/vsx/
  * 2010-10-03: OID<=249641, 182696 stars, from http://www.aavso.org/vsx/
  * 2010-10-10: OID<=249671, 182707 stars, from http://www.aavso.org/vsx/
  * 2010-10-17: OID<=249703, 182721 stars, from http://www.aavso.org/vsx/
  * 2010-10-24: OID<=249725, 182730 stars, from http://www.aavso.org/vsx/
  * 2010-10-31: OID<=250483, 183044 stars, from http://www.aavso.org/vsx/
  * 2010-11-07: OID<=250725, 183156 stars, from http://www.aavso.org/vsx/
  * 2010-11-14: OID<=250771, 183178 stars, from http://www.aavso.org/vsx/
  * 2010-11-21: OID<=250815, 183197 stars, from http://www.aavso.org/vsx/
  * 2010-11-28: OID<=251313, 183435 stars, from http://www.aavso.org/vsx/
  * 2010-12-05: OID<=251369, 183462 stars, from http://www.aavso.org/vsx/
  * 2010-12-12: OID<=251413, 183481 stars, from http://www.aavso.org/vsx/
  * 2010-12-19: OID<=251445, 183496 stars, from http://www.aavso.org/vsx/
  * 2010-12-26: OID<=251461, 183504 stars, from http://www.aavso.org/vsx/
  * 2011-01-02: OID<=251476, 183519 stars, from http://www.aavso.org/vsx/
  * 2011-01-09: OID<=251539, 181961 stars, from http://www.aavso.org/vsx/
  * 2011-01-16: OID<=251636, 181864 stars, from http://www.aavso.org/vsx/
  * 2011-01-23: OID<=251692, 181739 stars, from http://www.aavso.org/vsx/
  * 2011-01-30: OID<=251723, 181745 stars, from http://www.aavso.org/vsx/
  * 2011-02-06: OID<=251784, 181741 stars, from http://www.aavso.org/vsx/
  * 2011-02-13: OID<=252802, 182662 stars, from http://www.aavso.org/vsx/
  * 2011-02-27: OID<=252832, 182592 stars, from http://www.aavso.org/vsx/
  * 2011-03-06: OID<=252839, 182574 stars, from http://www.aavso.org/vsx/
  * 2011-03-13: OID<=253435, 183086 stars, from http://www.aavso.org/vsx/
  * 2011-03-20: OID<=253454, 183094 stars, from http://www.aavso.org/vsx/
  * 2011-03-27: OID<=255896, 185494 stars, from http://www.aavso.org/vsx/
  * 2011-04-03: OID<=255908, 185440 stars, from http://www.aavso.org/vsx/
  * 2011-04-10: OID<=256048, 185523 stars, from http://www.aavso.org/vsx/
  * 2011-04-17: OID<=256050, 185442 stars, from http://www.aavso.org/vsx/
  * 2011-04-25: OID<=256129, 185494 stars, from http://www.aavso.org/vsx/
  * 2011-05-01: OID<=256141, 185413 stars, from http://www.aavso.org/vsx/
  * 2011-05-08: OID<=256191, 185384 stars, from http://www.aavso.org/vsx/
  * 2011-05-15: OID<=256205, 185376 stars, from http://www.aavso.org/vsx/
  * 2011-05-22: OID<=256241, 185335 stars, from http://www.aavso.org/vsx/
  * 2011-05-29: OID<=256271, 185294 stars, from http://www.aavso.org/vsx/
  * 2011-06-05: OID<=256294, 185204 stars, from http://www.aavso.org/vsx/
  * 2011-06-12: OID<=268851, 197648 stars, from http://www.aavso.org/vsx/
  * 2011-06-19: OID<=268898, 197540 stars, from http://www.aavso.org/vsx/
  * 2011-06-26: OID<=269079, 197667 stars, from http://www.aavso.org/vsx/
  * 2011-07-03: OID<=269113, 197677 stars; addition of the "vsx_id.dat" file.
  * 2011-07-10: OID<=269757, 198313 stars, from http://www.aavso.org/vsx/
  * 2011-07-17: OID<=269810, 198347 stars, from http://www.aavso.org/vsx/
  * 2011-07-24: OID<=269838, 198374 stars, from http://www.aavso.org/vsx/
  * 2011-07-31: OID<=269850, 198351 stars, from http://www.aavso.org/vsx/
  * 2011-08-07: OID<=269859, 198332 stars, from http://www.aavso.org/vsx/
  * 2011-08-15: OID<=270028, 198481 stars, from http://www.aavso.org/vsx/
  * 2011-08-21: OID<=270070, 198476 stars, from http://www.aavso.org/vsx/
  * 2011-08-28: OID<=270212, 198585 stars, from http://www.aavso.org/vsx/
  * 2011-09-04: OID<=270232, 198557 stars, from http://www.aavso.org/vsx/
  * 2011-09-11: OID<=270273, 198569 stars, from http://www.aavso.org/vsx/
  * 2011-09-18: OID<=270302, 198545 stars, from http://www.aavso.org/vsx/
  * 2011-09-25: OID<=270340, 198521 stars, from http://www.aavso.org/vsx/
  * 2011-10-02: OID<=270412, 198568 stars, from http://www.aavso.org/vsx/
  * 2011-10-09: OID<=270415, 198571 stars, from http://www.aavso.org/vsx/
  * 2011-10-16: OID<=270624, 198765 stars, from http://www.aavso.org/vsx/
  * 2011-10-23: OID<=270685, 198797 stars, from http://www.aavso.org/vsx/
  * 2011-10-30: OID<=270733, 198841 stars, from http://www.aavso.org/vsx/
  * 2011-11-06: OID<=270771, 198870 stars, from http://www.aavso.org/vsx/
  * 2011-11-13: OID<=270811, 198907 stars, from http://www.aavso.org/vsx/
  * 2011-11-20: OID<=270889, 198956 stars, from http://www.aavso.org/vsx/
  * 2011-11-27: OID<=271317, 199296 stars, from http://www.aavso.org/vsx/
  * 2011-12-04: OID<=271341, 199275 stars, from http://www.aavso.org/vsx/
  * 2011-12-11: OID<=271640, 199557 stars, from http://www.aavso.org/vsx/
  * 2011-12-18: OID<=271657, 199560 stars, from http://www.aavso.org/vsx/
  * 2011-12-25: OID<=272481, 200372 stars, from http://www.aavso.org/vsx/
  * 2012-01-01: OID<=275522, 203354 stars, from http://www.aavso.org/vsx/
  * 2012-01-08: OID<=275571, 203368 stars, from http://www.aavso.org/vsx/
  * 2012-01-15: OID<=275642, 203403 stars, from http://www.aavso.org/vsx/
  * 2012-01-22: OID<=275690, 203438 stars, from http://www.aavso.org/vsx/
  * 2012-01-29: OID<=276849, 204572 stars, from http://www.aavso.org/vsx/
  * 2012-02-05: OID<=276908, 204590 stars, from http://www.aavso.org/vsx/
  * 2012-02-12: OID<=277937, 205581 stars, from http://www.aavso.org/vsx/
  * 2012-02-19: OID<=278069, 205673 stars, from http://www.aavso.org/vsx/
  * 2012-02-26: OID<=278151, 205726 stars, from http://www.aavso.org/vsx/
  * 2012-03-04: OID<=278257, 205810 stars, from http://www.aavso.org/vsx/
  * 2012-03-11: OID<=278323, 205856 stars, from http://www.aavso.org/vsx/
  * 2012-03-18: OID<=278382, 205868 stars, from http://www.aavso.org/vsx/
  * 2012-03-25: OID<=278494, 205939 stars, from http://www.aavso.org/vsx/
  * 2012-04-08: OID<=278885, 206258 stars, from http://www.aavso.org/vsx/
  * 2012-04-15: OID<=278928, 206257 stars, from http://www.aavso.org/vsx/
  * 2012-04-22: OID<=281963, 209250 stars, from http://www.aavso.org/vsx/
  * 2012-04-29: OID<=282010, 209285 stars, from http://www.aavso.org/vsx/
  * 2012-05-06: OID<=282037, 209264 stars, from http://www.aavso.org/vsx/
  * 2012-05-13: OID<=282225, 209381 stars, from http://www.aavso.org/vsx/
  * 2012-05-20: OID<=282302, 209389 stars, from http://www.aavso.org/vsx/
  * 2012-05-27: OID<=282680, 209735 stars, from http://www.aavso.org/vsx/
  * 2012-06-03: OID<=282745, 209780 stars, from http://www.aavso.org/vsx/
  * 2012-06-10: OID<=283031, 210024 stars, from http://www.aavso.org/vsx/
  * 2012-06-17: OID<=285160, 212132 stars, from http://www.aavso.org/vsx/
  * 2012-06-24: OID<=285223, 212154 stars, from http://www.aavso.org/vsx/
  * 2012-07-01: OID<=285312, 212226 stars, from http://www.aavso.org/vsx/
  * 2012-07-08: OID<=285336, 212205 stars, from http://www.aavso.org/vsx/
  * 2012-07-15: OID<=285355, 212168 stars, from http://www.aavso.org/vsx/
  * 2012-07-22: OID<=285381, 212158 stars, from http://www.aavso.org/vsx/
  * 2012-07-29: OID<=285336, 212205 stars, from http://www.aavso.org/vsx/
  * 2012-08-20: OID<=285745, 212399 stars, from http://www.aavso.org/vsx/
  * 2012-08-26: OID<=285791, 212430 stars, from http://www.aavso.org/vsx/
  * 2012-09-16: OID<=286025, 212668 stars, from http://www.aavso.org/vsx/
  * 2012-09-23: OID<=286082, 212722 stars, from http://www.aavso.org/vsx/
  * 2012-09-30: OID<=286217, 212835 stars, from http://www.aavso.org/vsx/
  * 2012-10-07: OID<=286266, 212850 stars, from http://www.aavso.org/vsx/
  * 2012-10-14: OID<=286366, 212937 stars, from http://www.aavso.org/vsx/
  * 2012-10-21: OID<=286426, 212991 stars, from http://www.aavso.org/vsx/
  * 2012-10-28: OID<=286575, 213136 stars, from http://www.aavso.org/vsx/
  * 2012-11-04: OID<=286599, 213155 stars, from http://www.aavso.org/vsx/
  * 2012-11-11: OID<=287179, 213722 stars, from http://www.aavso.org/vsx/
  * 2012-11-18: OID<=287272, 213781 stars, from http://www.aavso.org/vsx/
  * 2012-11-25: OID<=287344, 213827 stars, from http://www.aavso.org/vsx/
  * 2012-12-02: OID<=287507, 213933 stars, from http://www.aavso.org/vsx/
  * 2012-12-09: OID<=287611, 214028 stars, from http://www.aavso.org/vsx/
  * 2012-12-16: OID<=287684, 214056 stars, from http://www.aavso.org/vsx/
  * 2012-12-23: OID<=287713, 214059 stars, from http://www.aavso.org/vsx/
  * 2012-12-30: OID<=287952, 214287 stars, from http://www.aavso.org/vsx/
  * 2013-01-06: OID<=297190, 223508 stars, from http://www.aavso.org/vsx/
  * 2013-01-13: OID<=297262, 223540 stars, from http://www.aavso.org/vsx/
  * 2013-01-20: OID<=297312, 223571 stars, from http://www.aavso.org/vsx/
  * 2013-01-27: OID<=297343, 223544 stars, from http://www.aavso.org/vsx/
  * 2013-02-03: OID<=297385, 223555 stars, from http://www.aavso.org/vsx/
  * 2013-02-10: OID<=297475, 223636 stars, from http://www.aavso.org/vsx/
  * 2013-02-17: OID<=297522, 223665 stars, from http://www.aavso.org/vsx/
  * 2013-02-24: OID<=297579, 223716 stars, from http://www.aavso.org/vsx/
  * 2013-03-03: OID<=297833, 223960 stars, from http://www.aavso.org/vsx/
  * 2013-03-10: OID<=298249, 224363 stars, from http://www.aavso.org/vsx/
  * 2013-03-17: OID<=298332, 224446 stars, from http://www.aavso.org/vsx/
  * 2013-03-24:              224447 stars, from http://www.aavso.org/vsx/
  * 2013-03-31: OID<=300016, 226090 stars, from http://www.aavso.org/vsx/
  * 2013-04-07: OID<=300062, 226129 stars, from http://www.aavso.org/vsx/
  * 2013-04-14: OID<=300085, 226131 stars, from http://www.aavso.org/vsx/
  * 2013-04-21: OID<=305006, 231027 stars, from http://www.aavso.org/vsx/
  * 2013-04-28: OID<=305025, 231035 stars, from http://www.aavso.org/vsx/
  * 2013-05-05: OID<=305889, 231886 stars, from http://www.aavso.org/vsx/
  * 2013-05-12: OID<=305908, 231867 stars, from http://www.aavso.org/vsx/
  * 2013-05-19: OID<=305958, 231881 stars, from http://www.aavso.org/vsx/
  * 2013-05-26: OID<=306098, 231995 stars, from http://www.aavso.org/vsx/
  * 2013-06-02: OID<=306393, 232258 stars, from http://www.aavso.org/vsx/
  * 2013-06-09: OID<=306436, 232266 stars, from http://www.aavso.org/vsx/
  * 2013-06-16: OID<=306563, 232353 stars, from http://www.aavso.org/vsx/
  * 2013-06-23: OID<=306603, 232359 stars, from http://www.aavso.org/vsx/
  * 2013-06-30: OID<=317859, 243610 stars, from http://www.aavso.org/vsx/
  * 2013-07-07: OID<=318093, 243786 stars, from http://www.aavso.org/vsx/
  * 2013-07-14: OID<=318177, 243831 stars, from http://www.aavso.org/vsx/
  * 2013-07-21: OID<=318307, 243959 stars, from http://www.aavso.org/vsx/
  * 2013-07-28: OID<=318406, 244055 stars, from http://www.aavso.org/vsx/
  * 2013-08-04: OID<=318503, 244134 stars, from http://www.aavso.org/vsx/
  * 2013-08-11: OID<=322709, 248330 stars, from http://www.aavso.org/vsx/
  * 2013-08-18: OID<=322818, 248439 stars, from http://www.aavso.org/vsx/
  * 2013-08-25: OID<=322874, 248467 stars, from http://www.aavso.org/vsx/
  * 2013-09-01: OID<=322948, 248518 stars, from http://www.aavso.org/vsx/
  * 2013-09-08: OID<=355816, 281355 stars, from http://www.aavso.org/vsx/
  * 2013-09-15: OID<=355844, 281359 stars, from http://www.aavso.org/vsx/
  * 2013-09-22: OID<=356108, 281619 stars, from http://www.aavso.org/vsx/
  * 2013-09-29: OID<=356257, 281750 stars, from http://www.aavso.org/vsx/
  * 2013-10-06: OID<=356508, 282000 stars, from http://www.aavso.org/vsx/
  * 2013-10-14: OID<=356550, 282033 stars, from http://www.aavso.org/vsx/
  * 2013-10-21: OID<=356618, 282099 stars, from http://www.aavso.org/vsx/
  * 2013-10-27: OID<=358571, 284051 stars, from http://www.aavso.org/vsx/
  * 2013-11-03: OID<=358621, 284097 stars, from http://www.aavso.org/vsx/
  * 2013-11-10: OID<=358660, 284126 stars, from http://www.aavso.org/vsx/
  * 2013-11-18: OID<=358693, 284143 stars, from http://www.aavso.org/vsx/
  * 2013-11-24: OID<=358718, 284154 stars, from http://www.aavso.org/vsx/
  * 2013-12-02: OID<=358919, 284354 stars, from http://www.aavso.org/vsx/
  * 2013-12-09: OID<=358946, 284381 stars, from http://www.aavso.org/vsx/
  * 2013-12-17: OID<=359048, 284478 stars, from http://www.aavso.org/vsx/
  * 2013-12-22: OID<=359073, 284488 stars, from http://www.aavso.org/vsx/
  * 2013-12-29: OID<=359225, 284631 stars, from http://www.aavso.org/vsx/
  * 2014-01-05: OID<=359266, 284658 stars, from http://www.aavso.org/vsx/
  * 2014-01-13: OID<=359337, 284704 stars, from http://www.aavso.org/vsx/
  * 2014-01-26: OID<=359519, 284830 stars, from http://www.aavso.org/vsx/
  * 2014-02-02: OID<=359564, 284848 stars, from http://www.aavso.org/vsx/
  * 2014-02-10: OID<=359612, 284895 stars, from http://www.aavso.org/vsx/
  * 2014-02-17: OID<=359632, 284889 stars, from http://www.aavso.org/vsx/
  * 2014-02-24: OID<=359651, 285358 stars, from http://www.aavso.org/vsx/
  * 2014-03-03: OID<=359677, 285365 stars, from http://www.aavso.org/vsx/
  * 2014-03-03: OID<=359677, 285368 stars, from http://www.aavso.org/vsx/
  * 2014-03-10: OID<=359700, 285370 stars, from http://www.aavso.org/vsx/
  * 2014-03-17: OID<=359730, 285400 stars, from http://www.aavso.org/vsx/
  * 2014-03-24: OID<=359744, 285413 stars, from http://www.aavso.org/vsx/
  * 2014-03-31: OID<=359992, 285660 stars, from http://www.aavso.org/vsx/
  * 2014-04-07: OID<=360095, 285739 stars, from http://www.aavso.org/vsx/
  * 2014-04-14: OID<=360132, 285753 stars, from http://www.aavso.org/vsx/
  * 2014-04-22: OID<=360145, 285737 stars, from http://www.aavso.org/vsx/
  * 2014-04-29: OID<=360174, 285763 stars, from http://www.aavso.org/vsx/
  * 2014-05-05: OID<=360207, 285793 stars, from http://www.aavso.org/vsx/
  * 2014-05-12: OID<=360300, 285859 stars, from http://www.aavso.org/vsx/
  * 2014-05-19: OID<=360334, 285852 stars, from http://www.aavso.org/vsx/
  * 2014-06-16: OID<=398760, 324216 stars, from http://www.aavso.org/vsx/
  * 2014-06-30: OID<=398901, 324290 stars, from http://www.aavso.org/vsx/
  * 2014-07-21: OID<=399016, 324372 stars, from http://www.aavso.org/vsx/
  * 2014-08-04: OID<=399086, 324413 stars, from http://www.aavso.org/vsx/
  * 2014-08-19: OID<=399157, 324470 stars, from http://www.aavso.org/vsx/
  * 2014-09-01: OID<=399215, 324516 stars, from http://www.aavso.org/vsx/
  * 2014-09-08: OID<=399257, 324552 stars, from http://www.aavso.org/vsx/
  * 2014-09-15: OID<=399294, 324584 stars, from http://www.aavso.org/vsx/
  * 2014-09-22: OID<=399322, 324592 stars, from http://www.aavso.org/vsx/
  * 2014-09-29: OID<=399525, 324793 stars, from http://www.aavso.org/vsx/
  * 2014-10-08: OID<=399625, 324865 stars, from http://www.aavso.org/vsx/
  * 2014-10-12: OID<=399665, 324903 stars, from http://www.aavso.org/vsx/
  * 2014-10-20: OID<=399688, 324920 stars, from http://www.aavso.org/vsx/
  * 2014-11-03: OID<=399754, 324974 stars, from http://www.aavso.org/vsx/
  * 2014-11-10: OID<=399772, 324971 stars, from http://www.aavso.org/vsx/
  * 2014-11-17: OID<=399798, 324964 stars, from http://www.aavso.org/vsx/
  * 2014-11-24: OID<=399830, 324976 stars, from http://www.aavso.org/vsx/
  * 2014-12-01: OID<=399855, 324992 stars, from http://www.aavso.org/vsx/
  * 2014-12-08: OID<=399883, 325008 stars, from http://www.aavso.org/vsx/
  * 2014-12-15: OID<=399906, 325024 stars, from http://www.aavso.org/vsx/
  * 2014-12-22: OID<=399924, 325001 stars, from http://www.aavso.org/vsx/
  * 2014-12-29: OID<=399942, 325012 stars, from http://www.aavso.org/vsx/
  * 2015-01-05: OID<=399968, 325031 stars, from http://www.aavso.org/vsx/
  * 2015-01-12: OID<=399997, 325048 stars, from http://www.aavso.org/vsx/
  * 2015-01-19: OID<=400024, 325055 stars, from http://www.aavso.org/vsx/
  * 2015-02-02: OID<=400086, 325067 stars, from http://www.aavso.org/vsx/
  * 2015-02-09: OID<=400108, 325061 stars, from http://www.aavso.org/vsx/
  * 2015-02-16: OID<=400144, 325091 stars, from http://www.aavso.org/vsx/
  * 2015-02-16: OID<=400144, 325091 stars, from http://www.aavso.org/vsx/
  * 2015-03-03: OID<=400242, 325139 stars, from http://www.aavso.org/vsx/
  * 2015-03-09: OID<=400272, 325158 stars, from http://www.aavso.org/vsx/
  * 2015-03-16: OID<=400300, 325136 stars, from http://www.aavso.org/vsx/
  * 2015-03-26: OID<=400344, 325179 stars, from http://www.aavso.org/vsx/
  * 2015-03-30: OID<=400358, 325192 stars, from http://www.aavso.org/vsx/
  * 2015-04-07: OID<=400463, 325283 stars, from http://www.aavso.org/vsx/
  * 2015-04-13: OID<=400486, 325286 stars, from http://www.aavso.org/vsx/
  * 2015-04-20: OID<=400555, 325346 stars, from http://www.aavso.org/vsx/
  * 2015-04-27: OID<=400603, 325391 stars, from http://www.aavso.org/vsx/
  * 2015-05-04: OID<=409177, 333960 stars, from http://www.aavso.org/vsx/
  * 2015-05-11: OID<=409214, 333993 stars, from http://www.aavso.org/vsx/
  * 2015-05-18: OID<=409268, 334040 stars, from http://www.aavso.org/vsx/
  * 2015-05-26: OID<=409356, 334112 stars, from http://www.aavso.org/vsx/
  * 2015-06-01: OID<=409374, 334116 stars, from http://www.aavso.org/vsx/
  * 2015-06-08: OID<=409385, 334102 stars, from http://www.aavso.org/vsx/
  * 2015-06-10: OID<=409385, 334102 stars, from http://www.aavso.org/vsx/
  * 2015-06-22: OID<=409431, 334119 stars, from http://www.aavso.org/vsx/
  * 2015-06-29: OID<=409462, 334145 stars, from http://www.aavso.org/vsx/
  * 2015-07-05: OID<=409494, 334164 stars, from http://www.aavso.org/vsx/
  * 2015-07-12: OID<=409527, 334193 stars, from http://www.aavso.org/vsx/
  * 2015-07-19: OID<=409554, 334219 stars, from http://www.aavso.org/vsx/
  * 2015-07-27: OID<=409587, 334236 stars, from http://www.aavso.org/vsx/
  * 2015-08-04: OID<=409610, 334254 stars, from http://www.aavso.org/vsx/
  * 2015-08-17: OID<=409666, 334280 stars, from http://www.aavso.org/vsx/
  * 2015-08-24: OID<=409688, 334292 stars, from http://www.aavso.org/vsx/
  * 2015-09-01: OID<=409704, 334301 stars, from http://www.aavso.org/vsx/
  * 2015-09-07: OID<=409974, 334569 stars, from http://www.aavso.org/vsx/
  * 2015-09-14: OID<=409998, 334592 stars, from http://www.aavso.org/vsx/
  * 2015-09-21: OID<=410024, 334616 stars, from http://www.aavso.org/vsx/
  * 2015-09-28: OID<=410057, 334607 stars, from http://www.aavso.org/vsx/
  * 2015-10-05: OID<=410071, 334617 stars, from http://www.aavso.org/vsx/
  * 2015-10-12: OID<=410111, 334655 stars, from http://www.aavso.org/vsx/
  * 2015-10-19: OID<=410130, 334672 stars, from http://www.aavso.org/vsx/
  * 2015-10-27: OID<=410152, 334693 stars, from http://www.aavso.org/vsx/
  * 2015-11-02: OID<=410332, 334850 stars, from http://www.aavso.org/vsx/
  * 2015-11-09: OID<=410360, 334873 stars, from http://www.aavso.org/vsx/
  * 2015-11-16: OID<=410386, 334898 stars, from http://www.aavso.org/vsx/
  * 2015-11-23: OID<=410470, 334982 stars, from http://www.aavso.org/vsx/
  * 2015-11-30: OID<=417421, 341925 stars, from http://www.aavso.org/vsx/
  * 2015-12-07: OID<=417461, 341965 stars, from http://www.aavso.org/vsx/
  * 2015-12-14: OID<=417493, 341996 stars, from http://www.aavso.org/vsx/
  * 2015-12-29: OID<=418007, 342496 stars, from http://www.aavso.org/vsx/
  * 2016-01-11: OID<=469552, 393968 stars, from http://www.aavso.org/vsx/
  * 2016-01-18: OID<=469580, 393996 stars, from http://www.aavso.org/vsx/
  * 2016-01-25: OID<=469603, 394016 stars, from http://www.aavso.org/vsx/
  * 2016-02-01: OID<=469631, 394044 stars, from http://www.aavso.org/vsx/
  * 2016-02-15: OID<=469774, 394184 stars, from http://www.aavso.org/vsx/
  * 2016-02-22: OID<=469827, 394237 stars, from http://www.aavso.org/vsx/
  * 2016-02-29: OID<=469886, 394295 stars, from http://www.aavso.org/vsx/
  * 2016-03-07: OID<=470021, 394429 stars, from http://www.aavso.org/vsx/
  * 2016-03-14: OID<=470057, 394465 stars, from http://www.aavso.org/vsx/
  * 2016-03-21: OID<=470100, 394490 stars, from http://www.aavso.org/vsx/
  * 2016-04-04: OID<=470150, 394535 stars, from http://www.aavso.org/vsx/
  * 2016-04-18: OID<=470205, 394587 stars, from http://www.aavso.org/vsx/
  * 2016-04-25: OID<=470234, 394599 stars, from http://www.aavso.org/vsx/
  * 2016-05-09: OID<=470421, 394773 stars, from http://www.aavso.org/vsx/
  * 2016-05-23: OID<=470454, 394805 stars, from http://www.aavso.org/vsx/
  * 2016-05-30: OID<=470475, 394825 stars, from http://www.aavso.org/vsx/
  * 2016-06-06: OID<=472068, 396407 stars, from http://www.aavso.org/vsx/
  * 2016-06-13: OID<=472087, 396425 stars, from http://www.aavso.org/vsx/
  * 2016-06-20: OID<=473552, 397891 stars, from http://www.aavso.org/vsx/
  * 2016-06-27: OID<=473576, 397921 stars, from http://www.aavso.org/vsx/
  * 2016-07-04: OID<=473589, 397933 stars, from http://www.aavso.org/vsx/
  * 2016-07-26: OID<=473700, 398030 stars, from http://www.aavso.org/vsx/
  * 2016-08-08: OID<=473758, 398060 stars, from http://www.aavso.org/vsx/
  * 2016-08-16: OID<=473832, 398088 stars, from http://www.aavso.org/vsx/
  * 2016-08-22: OID<=473886, 398215 stars, from http://www.aavso.org/vsx/
  * 2016-08-29: OID<=473910, 398237 stars, from http://www.aavso.org/vsx/
  * 2016-09-05: OID<=473932, 398256 stars, from http://www.aavso.org/vsx/
  * 2016-09-12: OID<=473993, 398211 stars, from http://www.aavso.org/vsx/
  * 2016-09-26: OID<=474105, 398428 stars, from http://www.aavso.org/vsx/
  * 2016-10-03: OID<=474577, 398898 stars, from http://www.aavso.org/vsx/
  * 2016-10-10: OID<=474629, 398949 stars, from http://www.aavso.org/vsx/
  * 2016-10-25: OID<=474747, 399062 stars, from http://www.aavso.org/vsx/
  * 2016-11-02: OID<=474870, 399185 stars, from http://www.aavso.org/vsx/
  * 2016-11-07: OID<=475785, 400099 stars, from http://www.aavso.org/vsx/
  * 2016-11-14: OID<=475831, 400137 stars, from http://www.aavso.org/vsx/
  * 2016-11-21: OID<=475867, 400172 stars, from http://www.aavso.org/vsx/
  * 2016-11-28: OID<=0, 0 stars, from http://www.aavso.org/vsx/
  * 2016-11-28: OID<=400288, 400288 stars, from http://www.aavso.org/vsx/
  * 2016-12-06: OID<=0, 0 stars, from http://www.aavso.org/vsx/
  * 2016-12-06: OID<=400333, 400333 stars, from http://www.aavso.org/vsx/
  * 2016-12-13: OID<=400357, 400357 stars, from http://www.aavso.org/vsx/
  * 2017-01-02: OID<=400500, 400500 stars, from http://www.aavso.org/vsx/
  * 2017-01-09: OID<=400569, 400569 stars, from http://www.aavso.org/vsx/
  * 2017-01-17: OID<=400726, 400726 stars, from http://www.aavso.org/vsx/
  * 2017-01-23: OID<=400870, 400870 stars, from http://www.aavso.org/vsx/
  * 2017-01-30: OID<=400931, 400931 stars, from http://www.aavso.org/vsx/
  * 2017-02-06: OID<=400960, 400960 stars, from http://www.aavso.org/vsx/
  * 2017-02-13: OID<=400978, 400978 stars, from http://www.aavso.org/vsx/
  * 2017-02-27: OID<=401350, 401350 stars, from http://www.aavso.org/vsx/
  * 2017-03-06: OID<=401398, 401398 stars, from http://www.aavso.org/vsx/
  * 2017-03-13: OID<=401687, 401687 stars, from http://www.aavso.org/vsx/
  * 2017-03-20: OID<=401727, 401727 stars, from http://www.aavso.org/vsx/
  * 2017-03-27: OID<=397606, 397606 stars, from http://www.aavso.org/vsx/
  * 2017-04-03: OID<=397673, 397673 stars, from http://www.aavso.org/vsx/
  * 2017-04-10: OID<=397469, 397469 stars, from http://www.aavso.org/vsx/
  * 2017-04-18: OID<=397514, 397514 stars, from http://www.aavso.org/vsx/
  * 2017-04-24: OID<=397547, 397547 stars, from http://www.aavso.org/vsx/
  * 2017-05-02: OID<=397586, 397586 stars, from http://www.aavso.org/vsx/
  * 2017-05-09: OID<=397631, 397631 stars, from http://www.aavso.org/vsx/
  * 2017-05-15: OID<=397685, 397685 stars, from http://www.aavso.org/vsx/
  * 2017-05-22: OID<=397756, 397756 stars, from http://www.aavso.org/vsx/
  * 2017-05-29: OID<=397805, 397805 stars, from http://www.aavso.org/vsx/
  * 2017-06-12: OID<=398901, 398901 stars, from http://www.aavso.org/vsx/
  * 2017-06-19: OID<=399038, 399038 stars, from http://www.aavso.org/vsx/
  * 2017-06-26: OID<=432481, 432481 stars, from http://www.aavso.org/vsx/
  * 2017-07-03: OID<=432528, 432528 stars, from http://www.aavso.org/vsx/
  * 2017-07-10: OID<=432580, 432580 stars, from http://www.aavso.org/vsx/
  * 2017-07-10: OID<=512766, 432580 stars, from http://www.aavso.org/vsx/
  * 2017-08-07: OID<=512896, 432709 stars, from http://www.aavso.org/vsx/
  * 2017-08-14: OID<=512930, 432743 stars, from http://www.aavso.org/vsx/
  * 2017-08-28: OID<=513036, 432849 stars, from http://www.aavso.org/vsx/
  * 2017-09-04: OID<=513064, 432877 stars, from http://www.aavso.org/vsx/
  * 2017-09-11: OID<=513121, 432934 stars, from http://www.aavso.org/vsx/
  * 2017-09-18: OID<=545280, 465092 stars, from http://www.aavso.org/vsx/
  * 2017-09-25: OID<=545310, 465116 stars, from http://www.aavso.org/vsx/
  * 2017-10-02: OID<=545337, 465142 stars, from http://www.aavso.org/vsx/
  * 2017-10-09: OID<=545364, 465168 stars, from http://www.aavso.org/vsx/
  * 2017-10-16: OID<=545396, 465200 stars, from http://www.aavso.org/vsx/
  * 2017-11-06: OID<=549683, 465603 stars, from http://www.aavso.org/vsx/
  * 2017-11-13: OID<=549733, 465654 stars, from http://www.aavso.org/vsx/
  * 2017-11-20: OID<=549769, 469637 stars, from http://www.aavso.org/vsx/
  * 2017-11-28: OID<=554633, 474501 stars, from http://www.aavso.org/vsx/
  * 2017-12-04: OID<=554658, 474526 stars, from http://www.aavso.org/vsx/
  * 2017-12-11: OID<=554687, 474553 stars, from http://www.aavso.org/vsx/
  * 2017-12-18: OID<=554882, 474748 stars, from http://www.aavso.org/vsx/
  * 2018-01-08: OID<=555476, 475341 stars, from http://www.aavso.org/vsx/
  * 2018-01-15: OID<=555503, 475368 stars, from http://www.aavso.org/vsx/
  * 2018-01-22: OID<=555629, 475491 stars, from http://www.aavso.org/vsx/
  * 2018-01-29: OID<=555668, 475529 stars, from http://www.aavso.org/vsx/
  * 2018-02-05: OID<=608156, 528008 stars, from http://www.aavso.org/vsx/
  * 2018-02-12: OID<=608185, 528037 stars, from http://www.aavso.org/vsx/
  * 2018-02-19: OID<=608284, 528133 stars, from http://www.aavso.org/vsx/
  * 2018-02-26: OID<=608428, 528255 stars, from http://www.aavso.org/vsx/
  * 2018-03-12: OID<=608527, 527365 stars, from http://www.aavso.org/vsx/
  * 2018-03-19: OID<=611964, 530793 stars, from http://www.aavso.org/vsx/
  * 2018-03-26: OID<=612024, 530858 stars, from http://www.aavso.org/vsx/
  * 2018-04-03: OID<=612061, 530877 stars, from http://www.aavso.org/vsx/
  * 2018-04-09: OID<=612098, 530914 stars, from http://www.aavso.org/vsx/
  * 2018-04-16: OID<=612164, 530980 stars, from http://www.aavso.org/vsx/
  * 2018-04-23: OID<=612203, 531019 stars, from http://www.aavso.org/vsx/
  * 2018-05-01: OID<=621165, 539981 stars, from http://www.aavso.org/vsx/
  * 2018-05-07: OID<=621200, 540015 stars, from http://www.aavso.org/vsx/
  * 2018-05-22: OID<=621286, 540049 stars, from http://www.aavso.org/vsx/
  * 2018-05-28: OID<=621318, 540081 stars, from http://www.aavso.org/vsx/
  * 2018-06-04: OID<=621351, 540107 stars, from http://www.aavso.org/vsx/
  * 2018-06-11: OID<=621384, 540139 stars, from http://www.aavso.org/vsx/
  * 2018-06-18: OID<=621418, 540173 stars, from http://www.aavso.org/vsx/
  * 2018-06-25: OID<=621677, 540422 stars, from http://www.aavso.org/vsx/
  * 2018-07-10: OID<=621738, 540450 stars, from http://www.aavso.org/vsx/
  * 2018-07-16: OID<=621762, 540473 stars, from http://www.aavso.org/vsx/
  * 2018-07-23: OID<=623178, 541888 stars, from http://www.aavso.org/vsx/
  * 2018-07-30: OID<=623245, 541955 stars, from http://www.aavso.org/vsx/
  * 2018-08-06: OID<=623298, 541992 stars, from http://www.aavso.org/vsx/
  * 2018-09-03: OID<=623903, 542597 stars, from http://www.aavso.org/vsx/
  * 2018-09-10: OID<=624550, 543242 stars, from http://www.aavso.org/vsx/
  * 2018-09-17: OID<=624599, 543291 stars, from http://www.aavso.org/vsx/
  * 2018-09-24: OID<=624662, 543354 stars, from http://www.aavso.org/vsx/
  * 2018-10-01: OID<=624698, 543382 stars, from http://www.aavso.org/vsx/
  * 2018-10-08: OID<=624824, 543507 stars, from http://www.aavso.org/vsx/
  * 2018-10-15: OID<=624888, 543565 stars, from http://www.aavso.org/vsx/
  * 2018-10-29: OID<=625108, 543782 stars, from http://www.aavso.org/vsx/
  * 2018-11-05: OID<=625143, 543815 stars, from http://www.aavso.org/vsx/
  * 2018-11-19: OID<=625268, 543940 stars, from http://www.aavso.org/vsx/
  * 2018-11-26: OID<=625345, 544017 stars, from http://www.aavso.org/vsx/
  * 2018-12-03: OID<=625739, 544410 stars, from http://www.aavso.org/vsx/
  * 2018-12-17: OID<=625867, 544527 stars, from http://www.aavso.org/vsx/
  * 2019-01-15: OID<=683950, 602301 stars, from http://www.aavso.org/vsx/
  * 2019-01-21: OID<=684026, 602376 stars, from http://www.aavso.org/vsx/
  * 2019-02-04: OID<=684172, 602520 stars, from http://www.aavso.org/vsx/
  * 2019-02-18: OID<=684270, 602618 stars, from http://www.aavso.org/vsx/
  * 2019-02-26: OID<=684311, 602658 stars, from http://www.aavso.org/vsx/
  * 2019-03-04: OID<=684367, 602714 stars, from http://www.aavso.org/vsx/
  * 2019-03-11: OID<=686697, 605044 stars, from http://www.aavso.org/vsx/
  * 2019-03-25: OID<=686850, 605194 stars, from http://www.aavso.org/vsx/
  * 2019-04-01: OID<=686915, 605259 stars, from http://www.aavso.org/vsx/
  * 2019-04-08: OID<=687305, 605649 stars, from http://www.aavso.org/vsx/
  * 2019-04-15: OID<=687374, 605718 stars, from http://www.aavso.org/vsx/
  * 2019-04-24: OID<=687452, 605796 stars, from http://www.aavso.org/vsx/
  * 2019-04-29: OID<=687532, 605876 stars, from http://www.aavso.org/vsx/
  * 2019-05-06: OID<=687598, 605943 stars, from http://www.aavso.org/vsx/
  * 2019-05-21: OID<=687704, 606042 stars, from http://www.aavso.org/vsx/
  * 2019-05-27: OID<=689721, 608051 stars, from http://www.aavso.org/vsx/
  * 2019-06-03: OID<=689778, 608070 stars, from http://www.aavso.org/vsx/
  * 2019-06-11: OID<=689900, 608169 stars, from http://www.aavso.org/vsx/
  * 2019-06-17: OID<=702841, 621088 stars, from http://www.aavso.org/vsx/
  * 2019-07-23: OID<=838267, 756511 stars, from http://www.aavso.org/vsx/
  * 2019-07-29: OID<=844296, 738410 stars, from http://www.aavso.org/vsx/
  * 2019-08-12: OID<=844431, 738490 stars, from http://www.aavso.org/vsx/
  * 2019-08-19: OID<=844484, 738514 stars, from http://www.aavso.org/vsx/
  * 2019-08-26: OID<=844535, 738565 stars, from http://www.aavso.org/vsx/
  * 2019-09-02: OID<=844610, 738639 stars, from http://www.aavso.org/vsx/
  * 2019-09-09: OID<=844763, 738789 stars, from http://www.aavso.org/vsx/
  * 2019-09-16: OID<=844819, 738845 stars, from http://www.aavso.org/vsx/
  * 2019-09-23: OID<=1260102, 1152414 stars, from http://www.aavso.org/vsx/
  * 2019-09-30: OID<=1498739, 1390973 stars, from http://www.aavso.org/vsx/
  * 2019-10-21: OID<=1499491, 1391725 stars, from http://www.aavso.org/vsx/
  * 2019-10-28: OID<=1499527, 1391758 stars, from http://www.aavso.org/vsx/
  * 2019-11-04: OID<=1499652, 1391838 stars, from http://www.aavso.org/vsx/
  * 2019-11-12: OID<=1499712, 1391898 stars, from http://www.aavso.org/vsx/
  * 2019-11-12: OID<=1499712, 1391898 stars, from http://www.aavso.org/vsx/
  * 2020-01-06: OID<=1540236, 1432434 stars, from http://www.aavso.org/vsx/
  * 2020-01-13: OID<=1540282, 1432478 stars, from http://www.aavso.org/vsx/
  * 2020-01-20: OID<=1540335, 1432531 stars, from http://www.aavso.org/vsx/
  * 2020-01-20: OID<=1540335, 1432531 stars, from http://www.aavso.org/vsx/
  * 2020-01-27: OID<=1540367, 1432563 stars, from http://www.aavso.org/vsx/
  * 2020-02-03: OID<=1540564, 1432760 stars, from http://www.aavso.org/vsx/
  * 2020-02-24: OID<=1540762, 1432958 stars, from http://www.aavso.org/vsx/
  * 2020-03-02: OID<=1542874, 1435070 stars, from http://www.aavso.org/vsx/
  * 2020-03-11: OID<=1543023, 1435219 stars, from http://www.aavso.org/vsx/
  * 2020-03-23: OID<=1543691, 1435871 stars, from http://www.aavso.org/vsx/
  * 2020-04-14: OID<=1543848, 1436007 stars, from http://www.aavso.org/vsx/
  * 2020-04-20: OID<=1543868, 1435885 stars, from http://www.aavso.org/vsx/
  * 2020-05-04: OID<=1543939, 1435960 stars, from http://www.aavso.org/vsx/
  * 2020-05-18: OID<=1544074, 1436093 stars, from http://www.aavso.org/vsx/
  * 2020-06-02: OID<=1545480, 1437485 stars, from http://www.aavso.org/vsx/
  * 2020-06-08: OID<=1545527, 1437524 stars, from http://www.aavso.org/vsx/
  * 2020-06-08: OID<=0, 0 stars, from http://www.aavso.org/vsx/
  * 2020-06-08: OID<=1437524, 1437524 stars, from http://www.aavso.org/vsx/
  * 2020-06-22: OID<=1437703, 1437703 stars, from http://www.aavso.org/vsx/
  * 2020-06-29: OID<=1437767, 1437767 stars, from http://www.aavso.org/vsx/
  * 2020-07-06: OID<=1437812, 1437812 stars, from http://www.aavso.org/vsx/
  * 2020-07-13: OID<=1437860, 1437860 stars, from http://www.aavso.org/vsx/
  * 2020-08-03: OID<=1437979, 1437979 stars, from http://www.aavso.org/vsx/
  * 2020-08-10: OID<=1437999, 1437999 stars, from http://www.aavso.org/vsx/
  * 2020-08-24: OID<=1438053, 1438053 stars, from http://www.aavso.org/vsx/
  * 2020-08-31: OID<=1438148, 1438148 stars, from http://www.aavso.org/vsx/
  * 2020-09-21: OID<=1439317, 1439317 stars, from http://www.aavso.org/vsx/
  * 2020-10-05: OID<=2104068, 2104068 stars, from http://www.aavso.org/vsx/
  * 2020-10-19: OID<=2105083, 2105083 stars, from http://www.aavso.org/vsx/
  * 2020-11-16: OID<=2105369, 2105369 stars, from http://www.aavso.org/vsx/
  * 2020-11-30: OID<=2105461, 2105461 stars, from http://www.aavso.org/vsx/
  * 2020-12-14: OID<=2105535, 2105535 stars, from http://www.aavso.org/vsx/
  * 2021-01-11: OID<=2106065, 2106065 stars, from http://www.aavso.org/vsx/
  * 2021-01-25: OID<=2106117, 2106117 stars, from http://www.aavso.org/vsx/
  * 2021-02-08: OID<=2106208, 2106208 stars, from http://www.aavso.org/vsx/
  * 2021-02-22: OID<=2106294, 2106294 stars, from http://www.aavso.org/vsx/
  * 2021-03-08: OID<=2106341, 2106341 stars, from http://www.aavso.org/vsx/
  * 2021-03-22: OID<=2107721, 2107721 stars, from http://www.aavso.org/vsx/
  * 2021-04-06: OID<=2107848, 2107848 stars, from http://www.aavso.org/vsx/
  * 2021-04-19: OID<=2108278, 2108278 stars, from http://www.aavso.org/vsx/
  * 2021-05-03: OID<=2108338, 2108338 stars, from http://www.aavso.org/vsx/
  * 2021-05-17: OID<=2111941, 2111941 stars, from http://www.aavso.org/vsx/
  * 2021-05-31: OID<=2113100, 2113100 stars, from http://www.aavso.org/vsx/
  * 2021-06-14: OID<=2113164, 2113164 stars, from http://www.aavso.org/vsx/
  * 2021-06-28: OID<=2113624, 2113624 stars, from http://www.aavso.org/vsx/
  * 2021-07-26: OID<=2114229, 2114229 stars, from http://www.aavso.org/vsx/
  * 2021-08-09: OID<=2114280, 2114280 stars, from http://www.aavso.org/vsx/
  * 2021-09-06: OID<=2114889, 2114889 stars, from http://www.aavso.org/vsx/
  * 2021-09-20: OID<=2115009, 2115009 stars, from http://www.aavso.org/vsx/
  * 2021-10-11: OID<=2115461, 2115461 stars, from http://www.aavso.org/vsx/
  * 2021-10-18: OID<=2115487, 2115487 stars, from http://www.aavso.org/vsx/
  * 2021-11-02: OID<=2115536, 2115536 stars, from http://www.aavso.org/vsx/
  * 2021-11-15: OID<=2115593, 2115593 stars, from http://www.aavso.org/vsx/
  * 2021-12-13: OID<=2115796, 2115796 stars, from http://www.aavso.org/vsx/
  * 2022-01-24: OID<=2116317, 2116317 stars, from http://www.aavso.org/vsx/
  * 2022-02-07: OID<=2116371, 2116371 stars, from http://www.aavso.org/vsx/
  * 2022-02-21: OID<=2116650, 2116650 stars, from http://www.aavso.org/vsx/
  * 2022-03-07: OID<=2117272, 2117272 stars, from http://www.aavso.org/vsx/
  * 2022-03-21: OID<=2117403, 2117403 stars, from http://www.aavso.org/vsx/
  * 2022-04-19: OID<=2117467, 2117467 stars, from http://www.aavso.org/vsx/
================================================================================
(End)    Christopher Watson, Patrick Wils; Francois Ochsenbein       19-Apr-2022