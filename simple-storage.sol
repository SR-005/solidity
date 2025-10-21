// SPDX-License-Identifier: MIT

pragma solidity ^0.8.30;

contract SimpleStorage{
    uint public favnumber=5;
    bool favbool=false;
    string favstring="Sreeram";
    address favaddress = 0xCEaaa7a684f5FBBDF41B865e2945142340D82029;

    function store(uint number) public 
    {
        favnumber=number;
    }


    struct People
    {
        uint integer;
        string name;
    }

    //People public person=People({integer:1,name:"Archana"});
    People[] public peoplearray;

    //mapping
    mapping(string=>uint) public mappingname;

    //using memory in variable parameter makes it so that the value will be stored only during the execution of the program
    function addperson(uint functioninteger, string memory functionname) public
    {
        peoplearray.push(People({integer: functioninteger, name:functionname})); 
        mappingname[functionname]=functioninteger;
    }
}