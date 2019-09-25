import React, { useEffect } from 'react';
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'
import CardMedia from '@material-ui/core/CardMedia'
import Typography from '@material-ui/core/Typography'
import { Redirect } from 'react-router-dom';
import Button from '@material-ui/core/Button'
import Asistencia from './Asistencia';

import { makeStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';
import Backdrop from '@material-ui/core/Backdrop';
import Fade from '@material-ui/core/Fade';


const useStyles = makeStyles(theme => ({
  modal: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  paper: {
    backgroundColor: theme.palette.background.paper,
    border: '2px solid #000',
    boxShadow: theme.shadows[5],
    padding: theme.spacing(2, 4, 3),
  },
}));


const DetalleCurso = ({match}) => {

    const classes = useStyles();
    const [open, setOpen] = React.useState(false);
    const [open_des, setOpen_des] = React.useState(false);
    const [cursos, setCursos] = React.useState([]);
    const [curso, setCurso] = React.useState([]);
    const [redirect, setRedirect] = React.useState(false);
    const [esProfesor, setProfesor] = React.useState([]);
    const [clases, setClases] = React.useState([]);


    const handleOpen = () => {
      setOpen(true);
    };

    const handleClose = () => {
      setOpen(false);
    };  

    const handleOpen_des = () => {
      setOpen_des(true);
    };

    const handleClose_des = () => {
      setOpen_des(false);
    };  

    useEffect(() => {
      fetch(`http://192.168.1.43:8000/api/v1/cursos/${match.params.id}`,{
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`,
        }
      })
      .then(res => res.json())
      .then(json => {
        setCurso(json);
      })

      fetch('http://192.168.1.43:8000/api/v1/alumnos/'+ localStorage.getItem('documento') +'/cursos',{
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`,
        }
      })
      .then(res => res.json())
      .then(json => {
        setCursos(json);
      })

      fetch('http://192.168.1.43:8000/api/v1/profesores/'+ localStorage.getItem('documento'),{
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`,
        }
      })
      .then(res => res.json())
      .then(json => {
        setProfesor(json);
      })

      fetch(`http://192.168.1.43:8000/api/v1/cursos/${match.params.id}/clases`,{
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`,
        }
      })
      .then(res => res.json())
      .then(json => {
        setClases(json);
      })

    }, []);

    const inscribirse = () => {
      fetch(`http://192.168.1.43:8000/api/v1/cursos/${match.params.id}/`,{
        method: 'PUT',
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`,
          'Content-Type': 'application/json'
        },
        body: `{"add_doc_alumno":${localStorage.getItem('documento')}}`
      })
      .then(res => {
        if(res.status === 200){
          alert("Tu inscripcion ah sido registrada!");
          setOpen(false);
          setRedirect();
          window.location.reload(false);
        }
      })
    };

    const desinscribirse = () => {
      fetch(`http://192.168.1.43:8000/api/v1/cursos/${match.params.id}/`,{
        method: 'PUT',
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`,
          'Content-Type': 'application/json'
        },
        body: `{"remove_doc_alumno":38800940}`
      })
      .then(res => {
        if(res.status === 200){
          alert("Tu desinscripcion ah sido registrada!");
          setOpen_des(false);
          setRedirect();
          window.location.reload(false);
        }
      })
    };

    if(redirect){
      return <Redirect to="/"/>
    }else{
      return(
        <Card>
            <CardMedia style={{height:0, paddingTop: '56.25%'}}
            image={curso.imagen}
            title={curso.nombre}
            />
            <CardContent>
            <Typography gutterBottom variant="h5" component="h2">
              {curso.nombre}
            </Typography>
            <Typography variant="body2" color="textSecondary" component="p">
              {curso.descripcion}
            </Typography>
            </CardContent>
            <CardActions>
                {esProfesor ?
                  <Asistencia clases={clases} curso={curso}/>
                :
                  cursos.find( c => c.id === curso.id)?
                    <button type="button" onClick={handleOpen_des}>
                      desinscribirse
                    </button>
                  :
                    <button type="button" onClick={handleOpen}>
                      inscribirse
                    </button>
                }
                <Modal
                  aria-labelledby="transition-modal-title"
                  aria-describedby="transition-modal-description"
                  className={classes.modal}
                  open={open}
                  onClose={handleClose}
                  closeAfterTransition
                  BackdropComponent={Backdrop}
                  BackdropProps={{
                    timeout: 500,
                  }}
                >
                  <Fade in={open}>
                    <div className={classes.paper}>
                      <h2 id="transition-modal-title">inscripción</h2>
                      <p id="transition-modal-description">¿Esta seguro que desea inscribirse en este curso?</p>
                      <Button size="small" color="primary" onClick={inscribirse}>  
                          Inscribirse
                      </Button>
                    </div>
                  </Fade>
                </Modal>

                <Modal
                  aria-labelledby="transition-modal-title"
                  aria-describedby="transition-modal-description"
                  className={classes.modal}
                  open={open_des}
                  onClose={handleClose}
                  closeAfterTransition
                  BackdropComponent={Backdrop}
                  BackdropProps={{
                    timeout: 500,
                  }}
                >
                  <Fade in={open_des}>
                    <div className={classes.paper}>
                      <h2 id="transition-modal-title">desinscripción</h2>
                      <p id="transition-modal-description">¿Esta seguro que desea desinscribirse en este curso?</p>
                      <Button size="small" color="primary" onClick={desinscribirse}>  
                          Desinscribirse
                      </Button>
                    </div>
                  </Fade>
                </Modal>
            </CardActions>
        </Card>
      )
    }
}

export default DetalleCurso