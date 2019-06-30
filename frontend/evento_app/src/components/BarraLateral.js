import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import HomeIcon from '@material-ui/icons/Home';
import PeopleIcon from '@material-ui/icons/People';
import SchoolIcon from '@material-ui/icons/School';
import AccoutBoxIcon from '@material-ui/icons/AccountBox';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import { NavLink } from 'react-router-dom';
import { Divider } from '@material-ui/core';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';


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
              <ListItemText primary="Home"/>
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
          <NavLink to="/profesores">
            <ListItem button>
              <ListItemIcon>
                <PeopleIcon />
              </ListItemIcon>
              <ListItemText primary="Asistencia?" />
            </ListItem>
          </NavLink>
        </List>
        <Divider />
        <List>
          <ListItem button>
            <ListItemIcon>
              <AccoutBoxIcon />
            </ListItemIcon>
            <ListItemText primary="Configurar Perfil" />
          </ListItem>
          <ListItem button>
            <ListItemIcon>
              <SchoolIcon />
            </ListItemIcon>
            <ListItemText primary="Mis Cursos" />
          </ListItem>
          <ListItem button>
            <ListItemIcon>
              <ExitToAppIcon />
            </ListItemIcon>
            <ListItemText primary="Salir" />
          </ListItem>
        </List>
      </React.Fragment> 
    );
  }
}

export default BarraLateral;