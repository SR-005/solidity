// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TestVerification {
    mapping(address => bool) public verified;

    function setVerified(address user) public {
        verified[user] = true;
    }

    function isVerified(address user) public view returns (bool) {
        return verified[user];
    }
}
