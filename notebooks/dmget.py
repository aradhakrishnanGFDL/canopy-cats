{
 "cells": [
  {
   "cell_type": "raw",
   "id": "f0b5a24c-30b6-4c27-8aef-5da7c744415d",
   "metadata": {},
   "source": [
    "'''\n",
    "\n",
    " for simple dmget usage, just use this !dmget {file}\n",
    " #use following to wrap the dmget call for each path in the catalog\n",
    "\n",
    " #USAGE\n",
    "\n",
    " #Once you have this code in your working directory.\n",
    " \n",
    " import dmgetmagic \n",
    "\n",
    " dmstatus = cat.df[\"path\"].apply(dmgetmagic)\n",
    "\n",
    " BEFORE you do the above, it's a good idea to make sure the number of rows are reasonable to run dmget on. \n",
    " E.g. Limit your search to your field of interest and then issue the dmget. \n",
    "\n",
    " cat = col.search(experiment_id=expname_filter,frequency=frequency,modeling_realm=modeling_realm,\n",
    "                 source_id=model_filter,variable_id=variable_id_filter)\n",
    " \n",
    " More examples  https://github.com/aradhakrishnanGFDL/canopy-cats/tree/main/notebooks\n",
    "\n",
    " '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2011dd0e-31a5-43b8-9c7c-98c68ee56dd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def dmgetmagic(x):\n",
    "    cmd = 'dmget %s'% str(x) \n",
    "    return os.system(cmd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "918687c2-40ed-4277-b09f-d3f542e69362",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
