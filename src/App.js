import React, { Component } from "react";
import { Carousel, CarouselCaption, CarouselInner, CarouselItem, View, Mask , Navbar, NavbarBrand, NavbarNav, NavItem, NavLink, NavbarToggler, 
  Collapse, FormInline, Dropdown, DropdownToggle, DropdownMenu,  DropdownItem } from "mdbreact";

class App extends Component {

  state = {
    isOpen: false
  };

  toggleCollapse = this.setState({ isOpen: !this.state.isOpen });
  render() {
    return (
<div>
      <Navbar color="indigo" dark expand="md">
          <NavbarBrand>
            <strong className="white-text">Navbar</strong>
          </NavbarBrand>
          <NavbarToggler
            onClick={this.toggleCollapse}
          />
          <Collapse
            id="navbarCollapse3"
            isOpen={this.state.isOpen}
            navbar
          >
            <NavbarNav left>
              <NavItem active>
                <NavLink to="#!">Home</NavLink>
              </NavItem>
              <NavItem>
                <NavLink to="#!">Features</NavLink>
              </NavItem>
              <NavItem>
                <NavLink to="#!">Pricing</NavLink>
              </NavItem>
              <NavItem>
                <Dropdown>
                  <DropdownToggle nav caret>
                    <div className="d-none d-md-inline">Dropdown</div>
                  </DropdownToggle>
                  <DropdownMenu right>
                    <DropdownItem href="#!">Action</DropdownItem>
                    <DropdownItem href="#!">Another Action</DropdownItem>
                    <DropdownItem href="#!">Something else here</DropdownItem>
                    <DropdownItem href="#!">Something else here</DropdownItem>
                  </DropdownMenu>
                </Dropdown>
              </NavItem>
            </NavbarNav>
            <NavbarNav right>
              <NavItem>
                <FormInline waves>
                  <div className="md-form my-0">
                    <input
                      className="form-control mr-sm-2"
                      type="text"
                      placeholder="Search"
                      aria-label="Search"
                    />
                  </div>
                </FormInline>
              </NavItem>
            </NavbarNav>
          </Collapse>
      </Navbar>
      <Carousel activeItem={1} length={4} showControls={true} showIndicators={true} className="z-depth-1">
        <CarouselInner>
          <CarouselItem itemId="1">
            <View>
              <img className="d-block w-100" src="https://mdbootstrap.com/img/Photos/Slides/img%20(68).jpg" alt="First slide" />
              <Mask overlay="black-light" />
            </View>
            <CarouselCaption>
              <h3 className="h3-responsive">Light mask</h3>
              <p>First text</p>
            </CarouselCaption>
          </CarouselItem>
          <CarouselItem itemId="2">
            <View>
              <img className="d-block w-100" src="https://mdbootstrap.com/img/Photos/Slides/img%20(99).jpg" alt="Second slide" />
              <Mask overlay="black-strong" />
            </View>
            <CarouselCaption>
              <h3 className="h3-responsive">Strong mask</h3>
              <p>Second text</p>
            </CarouselCaption>
          </CarouselItem>
          <CarouselItem itemId="3">
            <View>
              <img className="d-block w-100" src="https://mdbootstrap.com/img/Photos/Slides/img%20(17).jpg" alt="Third slide" />
              <Mask overlay="black-slight" />
            </View>
            <CarouselCaption>
              <h3 className="h3-responsive">Slight mask</h3>
              <p>Third text</p>
            </CarouselCaption>
          </CarouselItem>
          <CarouselItem itemId="4">
            <View>
              <img className="d-block w-100" src="https://mdbootstrap.com/img/Photos/Slides/img%20%28143%29.jpg" alt="Mattonit's item" />
              <Mask overlay="black-light" />
            </View>
            <CarouselCaption>
              <h3 className="h3-responsive">Sopot Beach</h3>
              <p>Taken june 21th by @mattonit</p>
            </CarouselCaption>
          </CarouselItem>
        </CarouselInner>
      </Carousel>
      </div>
    );
  }
}

export default App;