import React from 'react'
import { Link } from 'react-router-dom'
import Button from '@material-ui/core/Button'
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'
import CardMedia from '@material-ui/core/CardMedia'
import Typography from '@material-ui/core/Typography'

import { makeStyles } from '@material-ui/core/styles';

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


const Curso = (props) => {
  
  const classes = useStyles();

  return(
      <div>
          { props.curso ? (
              <Card>
                  <CardMedia style={{height:0, paddingTop: '56.25%'}}
                  image={props.curso.imagen}
                  title={props.curso.nombre}
                  />
                  <CardContent>
                  <Typography gutterBottom variant="h5" component="h2">
                    {props.curso.nombre}
                  </Typography>
                  <Typography variant="body2" color="textSecondary" component="p">
                    {props.curso.slogan}
                  </Typography>
                  </CardContent>
                  <CardActions>
                      <Link to={`detalle_curso/${props.curso.id}`}>
                        <Button size="small" color="primary">
                            ver mas
                        </Button>
                      </Link>
                  </CardActions>
              </Card>
          ) : <h1> Hola :D </h1>}
      </div>
  )
}

export default Curso