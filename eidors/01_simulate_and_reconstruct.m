% Simulation first: learn the pipeline before the hardware exists.
% UNTESTED SKELETON. Compare with the EIDORS 2D tutorials.
run('path/to/eidors/startup.m');          % TODO: your EIDORS path

n_elec = 8;
imdl = mk_common_model('c2c2', n_elec);   % 2D circular model, 8 electrodes (check the name in the docs)
fmdl = imdl.fwd_model;

% Adjacent injection, adjacent measurement
% TODO: confirm the arguments of mk_stim_patterns in the EIDORS docs
fmdl.stimulation = mk_stim_patterns(n_elec, 1, [0 1], [0 1], {'no_meas_current'}, 1);
imdl.fwd_model = fmdl;

% Homogeneous and with a simulated object
img_h = mk_image(fmdl, 1);
v_h = fwd_solve(img_h);
% TODO: build an inhomogeneous image with a small "plastic" region, solve again
% TODO: reconstruct the difference image and show it (inv_solve, show_fem)
% TODO: check that v_h.meas has 40 values
