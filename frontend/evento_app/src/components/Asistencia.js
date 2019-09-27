import React from 'react';
import Grid from '@material-ui/core/Grid';
import TablaAsistencia from './TablaAsistencia';

export function Asistencia(props){
    return(
        <Grid container spacing={3}>
            { props.clases.map(claseActual => (
                <Grid item xs={12} sm={12} lg={12} xl={12}>
                <TablaAsistencia clase={claseActual} curso={props.curso} />
                </Grid>
            ))}
        </Grid>
    )
}

export default Asistencia;