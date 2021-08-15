import './Header.css';
import React, { useState } from 'react';
import { Collapse, Navbar, NavbarToggler, NavbarBrand, Nav, NavItem, NavLink } from 'reactstrap';

function Header() {
  const [collapsed, setCollapsed] = useState(true);

  const toggleNavbar = () => setCollapsed(!collapsed);

  return (
    <div class="header">
      <h1>Standard<span class="seagreen">Alpha</span></h1>
      
    </div>
  );
}

/*
      <Navbar color="faded" dark>
        <NavbarBrand href="/" className="mr-auto">StandardAlpha</NavbarBrand>
        <NavbarToggler onClick={toggleNavbar} className="mr-2" />
        <Collapse isOpen={!collapsed} navbar>
          <Nav navbar>
            <NavItem>
              <NavLink href="">Components</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="">GitHub</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
*/

export default Header;