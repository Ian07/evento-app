import React, { useEffect } from 'react';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import CursoGrid from './CursoGrid';
import { Redirect } from 'react-router-dom';
import { Link } from 'react-router-dom'
import Button from '@material-ui/core/Button'

const drawerWidth = 240;
const useStyles = makeStyles(theme => ({
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
      marginRight: 36,
    },
    menuButtonHidden: {
      display: 'none',
    },
    title: {
      flexGrow: 1,
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
  }));

export function Inicio(props) {
    const classes = useStyles();
    const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight);
    
    const [cursos, setCursos] = React.useState([]);

    useEffect(() => {
      
      fetch('http://192.168.1.43:8000/api/v1/alumnos/'+ props.documento +'/cursos',{
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`,
        }
      })
      .then(res => res.json())
      .then(json => {
        setCursos(json);
      })
    }, []);

    if(! props.estaLogueado){
      return <Redirect to="/"/>
    }else if(cursos.length == 0){  
      return(
        <div>
          <Typography variant="h3" component="h3" color="inherit" gutterBottom align="center">
            ¡Cursos en los que estoy inscripto!
          </Typography>
          <Typography variant="h6" component="h6" color="inherit" gutterBottom align="center">
            No te encuentras inscripto a ningún curso.
            <Link to={'/cursos'}>
              <Button size="small" color="primary">
                  ¡Inscribite!
              </Button>
            </Link>
          </Typography>
        </div>
      );
    }else{
      return(
          <div>
            <Typography variant="h3" component="h3" color="inherit" gutterBottom align="center">
              ¡Cursos en los que estoy inscripto!
            </Typography>
            <Typography variant="h6" component="h6" color="inherit" gutterBottom align="center">
              Las clases empiezan el 10 de Septiembre
            </Typography>
            <CursoGrid cursos={cursos}></CursoGrid>
          </div>
      );
    }
}

export default Inicio;