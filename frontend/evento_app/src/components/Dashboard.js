import React from 'react';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import Container from '@material-ui/core/Container';
import AccountCircle from '@material-ui/icons/AccountCircle';
import MenuItem from '@material-ui/core/MenuItem';
import Menu from '@material-ui/core/Menu';
import LinkMaterial from '@material-ui/core/Link';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import NotificationsIcon from '@material-ui/icons/Notifications';
import BarraLateral from './BarraLateral';
import SignIn from './basic_auth/SignIn';
import SignUp from './basic_auth/SignUp';
import MisCursos from './MisCursos';
import Cursos from './Cursos';
import Profesor from './Profesor';
import Inicio from './Inicio';
import { Route, BrowserRouter } from 'react-router-dom';
import MoreIcon from '@material-ui/icons/MoreVert';
import { Link } from 'react-router-dom';
import ModificarPerfil from './ModificarPerfil';
import DetalleCurso from './DetalleCurso';
import Asistencia from './Asistencia';
import TablaAsistencia from './TablaAsistencia';

function Firma() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Desarrollado por '}
      <LinkMaterial color="inherit" href="https://github.com/matiasacosta/">
        Matias Acosta
      </LinkMaterial>
      {' e '}
      <LinkMaterial color="inherit" href="https://github.com/Ian07/">
        Ian Mazzaglia
      </LinkMaterial>
      {' utilizando '}
      <LinkMaterial color="inherit" href="https://material-ui.com/">
        Material UI
      </LinkMaterial>
    </Typography>
  );
}

const drawerWidth = 240;

const useStyles = makeStyles(theme => ({
  grow: {
    flexGrow: 1,
  },
  root: {
    display: 'flex',
  },
  toolbar: {
    paddingRight: 24, // keep right padding when drawer closed
  },
  toolbarIcon: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: '0 8px',
    ...theme.mixins.toolbar,
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  menuButton: {
    marginRight: 1,
  },
  menuButtonHidden: {
    display: 'none',
  },
  title: {
    
  },
  drawerPaper: {
    position: 'relative',
    whiteSpace: 'nowrap',
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  drawerPaperClose: {
    overflowX: 'hidden',
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    width: theme.spacing(7),
    [theme.breakpoints.up('sm')]: {
      width: theme.spacing(9),
    },
  },
  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
  },
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4),
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 240,
  },
  sectionDesktop: {
    display: 'none',
    [theme.breakpoints.up('md')]: {
      display: 'flex',
    },
  },
  sectionMobile: {
    display: 'flex',
    [theme.breakpoints.up('md')]: {
      display: 'none',
    },
  },
}));

export default function Dashboard(props) {
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);
  const abrirDrawer = () => {
    setOpen(true);
  };
  const cerrarDrawer = () => {
    setOpen(false);
  };

  const [anchorEl, setAnchorEl] = React.useState(null);
  const [mobileMoreAnchorEl, setMobileMoreAnchorEl] = React.useState(null);

  const isMenuOpen = Boolean(anchorEl);
  const isMobileMenuOpen = Boolean(mobileMoreAnchorEl);

  function handleProfileMenuOpen(event) {
    setAnchorEl(event.currentTarget);
  }

  function handleMobileMenuClose() {
    setMobileMoreAnchorEl(null);
  }

  function handleMenuClose() {
    setAnchorEl(null);
    handleMobileMenuClose();
  }

  function handleMobileMenuOpen(event) {
    setMobileMoreAnchorEl(event.currentTarget);
  }

  const menuId = 'primary-search-account-menu';
  const renderMenu = (
    <Menu
      anchorEl={anchorEl}
      anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
      id={menuId}
      keepMounted
      transformOrigin={{ vertical: 'top', horizontal: 'right' }}
      open={isMenuOpen}
      onClose={handleMenuClose}
    >
      {props.estaLogueado ?
        <MenuItem onClick={ () => {handleMenuClose() ; props.handleLogout()}}>Cerrar Sesión</MenuItem>
      : 
        <div>
          <Link to="/iniciar_sesion"><MenuItem onClick={handleMenuClose}>Iniciar Sesión</MenuItem></Link>
          <Link to="/registrarse"><MenuItem onClick={handleMenuClose}>Registrarse</MenuItem></Link>
        </div>
      }
      
    </Menu>
  );

  const mobileMenuId = 'primary-search-account-menu-mobile';
  const renderMobileMenu = (
    <Menu
      anchorEl={mobileMoreAnchorEl}
      anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
      id={mobileMenuId}
      keepMounted
      transformOrigin={{ vertical: 'top', horizontal: 'right' }}
      open={isMobileMenuOpen}
      onClose={handleMobileMenuClose}
    >
      <MenuItem onClick={handleProfileMenuOpen}>
        <IconButton
          aria-label="Account of current user"
          aria-controls="primary-search-account-menu"
          aria-haspopup="true"
          color="inherit"
        >
          <AccountCircle />
        </IconButton>
        {props.estaLogueado ?
          <p>{props.nombreUsuario}</p>
          :
          <p>Usuario</p>
        }
      </MenuItem>
    </Menu>
  );

  return (
    <div className={classes.root}>
      <BrowserRouter>
      <CssBaseline />
      <AppBar position="absolute" className={clsx(classes.appBar, open && classes.appBarShift)}>
        <Toolbar className={classes.toolbar}>
          {props.estaLogueado &&
            <IconButton
            edge="start"
            color="inherit"
            aria-label="Abrir drawer"
            onClick={abrirDrawer}
            className={clsx(classes.menuButton, open && classes.menuButtonHidden)}
            >
              <MenuIcon />
            </IconButton>
          }
          <Typography variant="h6" color="inherit" noWrap className={classes.title}>
            Escuela de Informática 2019
          </Typography>
          <div className={classes.grow} />
          <div className={classes.sectionDesktop}>
            <IconButton
              edge="end"
              aria-label="Account of current user"
              aria-controls={menuId}
              aria-haspopup="true"
              onClick={handleProfileMenuOpen}
              color="inherit"
            >
              <AccountCircle />
            </IconButton>
            {props.estaLogueado ?
              <p>{props.nombreUsuario}</p>
              :
              <p>Usuario</p>
            }
          </div>
          <div className={classes.sectionMobile}>
            <IconButton
              aria-label="Show more"
              aria-controls={mobileMenuId}
              aria-haspopup="true"
              onClick={handleMobileMenuOpen}
              color="inherit"
            >
              <MoreIcon />
            </IconButton>
          </div>
        </Toolbar>
      </AppBar>
      {renderMobileMenu}
      {renderMenu}
        <Drawer
          variant="temporary"
          classes={{
            paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
          }}
          open={open}
        >
          <div className={classes.toolbarIcon}>
            <IconButton onClick={cerrarDrawer}>
              <ChevronLeftIcon />
            </IconButton>
          </div>
          <Divider />
          <BarraLateral cerrarDrawer={cerrarDrawer} estaLogueado={props.estaLogueado}/>
        </Drawer>
        <main className={classes.content}>
          <div className={classes.appBarSpacer} />
          <Container maxWidth="lg" className={classes.container}>
            { /* Esto despues se mejora */ }
            
            <Route exact path="/" component={Inicio}/>

            <Route path="/cursos" render={() => <Cursos estaLogueado={props.estaLogueado}/>}/>
            <Route path="/mi_curso" render={() => <MisCursos documento={props.documento} estaLogueado={props.estaLogueado}/>}/>
            <Route path="/iniciar_sesion" render={() => <SignIn handleLogin={props.handleLogin} errores={props.erroresLogin} estaLogueado={props.estaLogueado}/>}/>
            <Route path="/detalle_curso/:id" component={DetalleCurso}/>
            <Route path="/registrarse" render={() => <SignUp handleSignUp={props.handleSignUp} errores={props.erroresSignup}/>}/>
            <Route path="/modificar_perfil" render={() => <ModificarPerfil handleModificarPerfil={props.handleModificarPerfil} 
            errores={props.erroresModificacion}
            nombreUsuario={props.nombreUsuario}
            emailUsuario={props.emailUsuario} 
            estaLogueado={props.estaLogueado}
            />}/>
          </Container>
          <Firma />
        </main>
      </BrowserRouter>  
    </div>
  );
}