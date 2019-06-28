import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import HomeIcon from '@material-ui/icons/Home';
import SchoolIcon from '@material-ui/icons/School';
import AccoutBoxIcon from '@material-ui/icons/AccountBox';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import PersonAddIcon from '@material-ui/icons/PersonAdd';
import { NavLink } from 'react-router-dom';
import { Divider } from '@material-ui/core';
import List from '@material-ui/core/List';


class BarraLateral extends React.Component{

  render(){
    return(
      <React.Fragment>
        <List onClick={this.props.cerrarDrawer}>
          <NavLink to="/">
            <ListItem button>
              <ListItemIcon>
                <HomeIcon />
              </ListItemIcon>
              <ListItemText primary="Inicio"/>
            </ListItem>
          </NavLink>
          <NavLink to="/cursos">
            <ListItem button>
              <ListItemIcon>
                <DashboardIcon />
              </ListItemIcon>
              <ListItemText primary="Cursos" />
            </ListItem>
          </NavLink>  
        </List>
        <Divider />
        {
          this.props.estaLogueado ?
          <List onClick={this.props.cerrarDrawer}>
            <NavLink to="/cursos">
              <ListItem button>
                <ListItemIcon>
                  <AccoutBoxIcon />
                </ListItemIcon>
                <ListItemText primary="Configurar Perfil" />
              </ListItem>
            </NavLink>  
            <NavLink to="/mis_cursos">
              <ListItem button>
                <ListItemIcon>
                  <SchoolIcon />
                </ListItemIcon>
                <ListItemText primary="Mis Cursos" />
              </ListItem>
            </NavLink>  
            <NavLink to="/logout">
              <ListItem button>
                <ListItemIcon>
                  <ExitToAppIcon />
                </ListItemIcon>
                <ListItemText primary="Salir" />
              </ListItem>
            </NavLink>
          </List>
          :
          <List onClick={this.props.cerrarDrawer}>
            <NavLink to="/iniciar_sesion">
              <ListItem button>
                <ListItemIcon>
                  <AccoutBoxIcon />
                </ListItemIcon>
                <ListItemText primary="Iniciar Sesión" />
              </ListItem>
            </NavLink>  
            <NavLink to="/registrarse">
              <ListItem button>
                <ListItemIcon>
                  <PersonAddIcon />
                </ListItemIcon>
                <ListItemText primary="Registrarse" />
              </ListItem>
            </NavLink>  
          </List>
        }
      </React.Fragment> 
    );
  }
}

export default BarraLateral;