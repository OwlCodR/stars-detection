package main

import (
	"bufio"
	"database/sql"
	"strconv"
	"strings"

	"fmt"
	"os"

	_ "github.com/lib/pq"
)

// Byte-by-byte Description of file: vsx.dat
// --------------------------------------------------------------------------------
//    Bytes Format Units   Label    Explanations
// --------------------------------------------------------------------------------
//    1-  7  I7    ---     OID      Internal identifier, can be used to
//                                  link out to the VSX database (1)
//    9- 38  A30   ---     Name     Variable star identifier
//       40  I1    ---     V        [0,3] Variability flag (2)
//   42- 50  F9.5  deg     RAdeg    Right ascension (J2000)
//   52- 60  F9.5  deg     DEdeg    Declination (J2000)
//   62- 91  A30   ---     Type     Variability type, as in GCVS catalog
//       94  A1    ---   l_max      Limit flag on max
//   95-100  F6.3  mag     max      ? Magnitude at maximum, or amplitude
//      101  A1    ---   u_max      Uncertainty flag on max
//  102-107  A6    ---   n_max      Passband on max magnitude (4)
//      109  A1    ---   f_min      [(] '(' indicates an amplitude
//      110  A1    ---   l_min      Limit flag on min
//  111-116  F6.3  mag     min      ? Magnitude at minimum, or amplitude
//      117  A1    ---   u_min      Uncertainty flag on min
//  118-123  A6    ---   n_min      Passband on min magnitude (4)
//  125-136  F12.4 d       Epoch    ? Epoch of maximum or minimum (HJD)
//      137  A1    ---   u_Epoch    [:)] Uncertainty flag (:) on epoch
//      139  A1    ---   l_Period   [<>(] Limit flag on period (3)
//  140-155 F16.10 d       Period   ? Period of the variable in days
//  156-158  A3    ---   u_Period   [:)*/N2 ] Uncertainty flag on Period (3)

/*
	1-7     I7     ---      OID      Internal identifier, can be used to
	9-38    A30    ---      Name     Variable star identifier
	40      I1     ---      V        [0,3] Variability flag (2)
	42- 50  F9.5   deg      RAdeg    Right ascension (J2000)
	52- 60  F9.5   deg      DEdeg    Declination (J2000)
	62- 91  A30    ---      Type     Variability type, as in GCVS catalog
	140-155 F16.10  d       Period   ? Period of the variable in days
*/
type vsxdat_line struct {
	OID    uint64
	Name   string
	V      int
	RAdeg  float64
	DEdeg  float64
	Type   string
	Period float64
}

func Parse() error {
	// open database
	db, err := sql.Open("postgres",
		fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
			"localhost",
			5432,
			"star_admin",
			"stars",
			"star_db"))
	if err != nil {
		return err
	}
	defer db.Close()

	// open vsx.dat file
	file, err := os.Open("../database/vsx.dat")
	if err != nil {
		return err
	}
	defer file.Close()

	// read line by line
	scanner := bufio.NewScanner(file)
	// optionally, resize scanner's capacity for lines over 64K
	const maxCapacity int = 256 // your required line length
	buf := make([]byte, maxCapacity)
	scanner.Buffer(buf, maxCapacity)
	// read

	// init variable
	var line vsxdat_line
	var str string
	i := 0
	j := 0
	k := 0
	var danger bool = true // danger state when we are in the cicle for defer function
	defer func() {
		if danger {
			fmt.Println(fmt.Sprintf("Debug info string number %d, str = '%s'.", i, str), []byte(str))
		} else {
			fmt.Println(fmt.Sprintf("Parsed %d lines", i))
		}
	}()

	for scanner.Scan() {
		// if i == 10 {
		// 	break
		// }

		str_line := []byte(scanner.Text())

		if len(scanner.Text()) < 94 {
			i += 1
			k += 1

			continue
		}

		// values
		str = strings.ReplaceAll(strings.ReplaceAll(string(str_line[0:7]), " ", ""), "\x00", "")
		if str == "" {
			i += 1
			continue
		}
		line.OID, err = strconv.ParseUint(str, 0, 64)
		if err != nil {
			return err
		}

		line.Name = strings.ReplaceAll(strings.ReplaceAll(string(str_line[8:38]), " ", ""), "\x00", "")

		str = strings.ReplaceAll(strings.ReplaceAll(string(str_line[39]), " ", ""), "\x00", "")
		if str == "" {
			i += 1
			continue
		}
		line.V, err = strconv.Atoi(str)
		if err != nil {
			return err
		}

		str = strings.ReplaceAll(strings.ReplaceAll(string(str_line[41:50]), " ", ""), "\x00", "")
		if str == "" {
			i += 1
			continue
		}
		line.RAdeg, err = strconv.ParseFloat(str, 64)
		if err != nil {
			return err
		}

		str = strings.ReplaceAll(strings.ReplaceAll(string(str_line[51:60]), " ", ""), "\x00", "")
		if str == "" {
			i += 1
			continue
		}
		line.DEdeg, err = strconv.ParseFloat(str, 64)
		if err != nil {
			return err
		}

		line.Type = strings.ReplaceAll(strings.ReplaceAll(string(str_line[61:91]), " ", ""), "\x00", "")

		if len(scanner.Text()) < 139 {
			i += 1
			j += 1

			// _, err = db.Exec(fmt.Sprintf("INSERT INTO vsx_dat_stars (oid, name, v, radeg, dedeg, type) "+
			// 	"VALUES (%d, '%s', %d, %.6f, %.6f, '%s');",
			// 	line.OID,
			// 	line.Name,
			// 	line.V,
			// 	line.RAdeg,
			// 	line.DEdeg,
			// 	line.Type,
			// ))

			continue
		}

		str = strings.ReplaceAll(strings.ReplaceAll(string(str_line[139:155]), " ", ""), "\x00", "")
		if str == "" {
			i += 1
			continue
		}
		line.Period, err = strconv.ParseFloat(str, 64)
		if err != nil {
			return err
		}

		// if i == 500 {
		// 	fmt.Println(line.OID)
		// 	fmt.Println(line.Name)
		// 	fmt.Println(line.V)
		// 	fmt.Println(line.RAdeg)
		// 	fmt.Println(line.DEdeg)
		// 	fmt.Println(line.Type)
		// 	fmt.Println(line.Period)
		// }

		// _, err = db.Exec(fmt.Sprintf("INSERT INTO vsx_dat_stars (oid, name, v, radeg, dedeg, type, period) "+
		// 	"VALUES (%d, '%s', %d, %.6f, %.6f, '%s', %.8f);",
		// 	line.OID,
		// 	line.Name,
		// 	line.V,
		// 	line.RAdeg,
		// 	line.DEdeg,
		// 	line.Type,
		// 	line.Period,
		// ))

		i += 1
	}
	if err := scanner.Err(); err != nil {
		return err
	}
	danger = false

	fmt.Println("Without period", j, "lines")
	fmt.Println("Drop", k, "lines")

	return nil
}

func main() {
	err := Parse()
	if err != nil {
		fmt.Println(err.Error())
	}
}
